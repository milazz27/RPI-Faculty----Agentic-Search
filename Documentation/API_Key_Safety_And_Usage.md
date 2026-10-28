# Storing API Keys Safely with a `.env` File (Python + Git)

**Core rule:** an API key is a password. It never goes in source code, never gets committed, and never gets pasted into chats, screenshots, or logs.

> Naming note: the standard filename is `.env`, not `.environment`. Tooling (python-dotenv, Docker, most `.gitignore` templates) expects `.env`.

---

## 1. Create the `.env` file

In your project root:

```
# .env
OPENAI_API_KEY=sk-your-real-key-here
DATABASE_URL=postgres://user:pass@localhost/db
```

Format rules:
- One `NAME=value` per line
- No spaces around `=`
- Quotes are optional unless the value contains spaces or `#`
- `#` starts a comment

Lock down file permissions (macOS/Linux) so only you can read it:

```bash
chmod 600 .env
```

---

## 2. Protect it from Git *before* anything else

**Do this before your first `git add`.** Order matters: once a secret is committed, it lives in history even if you delete it later.

```bash
echo ".env" >> .gitignore
```

A safer `.gitignore` entry set (catches variants like `.env.local`) while still allowing the template file:

```gitignore
.env
.env.*
!.env.example
```

Verify Git is actually ignoring it:

```bash
git check-ignore -v .env      # should print the matching .gitignore rule
git status                    # .env must NOT appear
```

### Commit a template instead

Create `.env.example` with **fake placeholder values** so teammates (and future you) know what variables are needed:

```
# .env.example
OPENAI_API_KEY=your-key-here
DATABASE_URL=postgres://user:pass@localhost/db
```

This file *is* committed. It must never contain a real secret.

### Optional: ignore `.env` globally

Protects you across every repo, including ones where you forget:

```bash
git config --global core.excludesfile ~/.gitignore_global
echo ".env" >> ~/.gitignore_global
```

---

## 3. Load the key in Python

Install python-dotenv:

```bash
pip install python-dotenv
```

### Basic usage

```python
import os
from dotenv import load_dotenv

load_dotenv()  # reads .env into environment variables

api_key = os.environ["OPENAI_API_KEY"]  # raises KeyError if missing
```

### Fail fast with a clear message

```python
import os
from dotenv import load_dotenv

load_dotenv()

def require_env(name: str) -> str:
    value = os.getenv(name)
    if not value:
        raise RuntimeError(f"Missing required environment variable: {name}")
    return value

API_KEY = require_env("OPENAI_API_KEY")
```

### Using it in a request

```python
import requests

resp = requests.get(
    "https://api.example.com/data",
    headers={"Authorization": f"Bearer {API_KEY}"},
    timeout=10,
)
```

### Notes
- `os.environ["X"]` fails loudly if missing; `os.getenv("X")` returns `None`. Prefer the loud version for required keys.
- `load_dotenv()` searches from the calling file's directory upward. If it can't find your file, pass a path: `load_dotenv("/path/to/.env")`.
- By default, variables already set in the real environment win over `.env` values. They are only overwritten if you pass `load_dotenv(override=True)`. The default is the right one for production.
- Call `load_dotenv()` once, at your program's entry point, not in every module.

---

## 4. Keep the key out of everywhere else

| Leak path | Prevention |
|---|---|
| `print()` / logs | Never print keys or full request headers. Log `key[:4] + "..."` at most. |
| Error tracebacks | Don't put the key in exception messages or f-strings that may be logged. |
| Jupyter notebooks | Never display the key in a cell; **clear outputs** before committing `.ipynb` files. |
| Docker images | Add `.env` to `.dockerignore`; pass secrets at runtime (`--env-file`, orchestrator secrets), not via `COPY`. |
| Screenshots / pasted code | Redact before sharing, including in AI chats and forums. |
| Frontend / client-side code | Never. Anything shipped to a browser is public. Call APIs from a backend. |
| Hardcoded fallbacks | Avoid `os.getenv("KEY", "sk-real-key")`. Defaults should never be real secrets. |

---

## 5. Git safety: prevention

### Pre-commit secret scanning

Catch secrets *before* they're committed:

```bash
pip install pre-commit
```

`.pre-commit-config.yaml`:

```yaml
repos:
  - repo: https://github.com/gitleaks/gitleaks
    rev: v8.18.4          # pin to the latest release
    hooks:
      - id: gitleaks
```

```bash
pre-commit install
```

### GitHub-side protections

On your repo: **Settings → Code security** (or "Advanced Security"):
- Enable **Secret scanning**
- Enable **Push protection** (blocks pushes containing detected secrets)

Many providers (OpenAI, AWS, GitHub, etc.) also auto-revoke keys that GitHub detects in public repos, but don't rely on that.

### Good habits
- Review `git diff --staged` before every commit.
- Prefer `git add <specific files>` over `git add .` / `git add -A`.
- Use **private** repos for anything experimental, but still treat secrets as if the repo could become public.

---

## 6. If you accidentally committed a key

**Assume it's compromised the moment it's pushed.** Bots scrape GitHub within seconds.

**Step 1: Revoke/rotate the key immediately** in the provider's dashboard. This is the only step that actually fixes the problem. Do it first, before cleaning Git.

**Step 2: Check the provider's usage logs** for activity you don't recognize.

**Step 3: Remove it from the repo going forward:**

```bash
git rm --cached .env
echo ".env" >> .gitignore
git commit -m "Stop tracking .env"
```

> This does **not** remove the key from past commits. It's still in history.

**Step 4: Scrub history** (optional once the key is revoked, but good hygiene):

```bash
pip install git-filter-repo
git filter-repo --invert-paths --path .env
git push --force --all
```

Alternative: [BFG Repo-Cleaner](https://rtyley.github.io/bfg-repo-cleaner/). Force-pushing rewrites history, so tell collaborators to re-clone. Forks and cached copies may still hold the old data, which is why rotation (Step 1) matters most.

---

## 7. Beyond local development

`.env` files are for **local dev**. For anything deployed:

- **GitHub Actions:** Settings → Secrets and variables → Actions, then reference as `${{ secrets.OPENAI_API_KEY }}`.
- **Cloud hosting:** use the platform's secret manager (AWS Secrets Manager, GCP Secret Manager, Azure Key Vault, Vercel/Heroku/Render env settings).
- **Least privilege:** create keys with the narrowest scope the provider offers.
- **Separate keys** for dev, staging, and production.
- **Spending/usage limits:** set caps so a leaked key has bounded damage.
- **Rotate periodically**, and immediately when someone leaves a project.

---

## Quick checklist

- [ ] Key lives only in `.env` (not in code, not in notebooks)
- [ ] `.env` is in `.gitignore` **before** the first commit
- [ ] `git check-ignore -v .env` confirms it's ignored
- [ ] `.env.example` committed with placeholders only
- [ ] `chmod 600 .env`
- [ ] Python loads via `load_dotenv()` + `os.environ[...]`
- [ ] Secret scanning / push protection enabled on GitHub
- [ ] Pre-commit hook (gitleaks) installed
- [ ] Deployed apps use a secret manager, not a `.env` file
- [ ] Plan known: **rotate first**, clean history second