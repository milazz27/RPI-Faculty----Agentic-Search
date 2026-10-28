# Guide to Contributing to GitHub For This Project

### Beginning Requirements:
1. Download VS Code
   - Installation links for Windows, Mac, Linux: https://code.visualstudio.com/download
2. Create an Account on GitHub
   - https://github.com/
3. Install Git
   - Git is the tool VS Code uses behind the scenes to clone, commit, and push.
   - Check if you already have it: open a terminal and run `git --version`. If a version number appears, skip this step.
   - Windows: download the installer from https://git-scm.com/downloads, run it, and keep the default options by clicking **Next** through each screen.
   - Mac: run `git --version` in Terminal. If Git is missing, macOS will prompt you to install the Command Line Tools, so click **Install**.
   - Restart VS Code after installing so it detects Git.
   - One-time setup: run these two commands, using the same email as your GitHub account:
     - `git config --global user.name "Your Name"`
     - `git config --global user.email "you@example.com"`
4. Download the Extension 'GitHub Pull Requests'
   - To do this, navigate to the extension tab on the left side of the screen and type the name into the search bar
   - ![alt text](image-1.png)
   - Click **Install**, then click the **Accounts** icon in the bottom-left of VS Code and choose **Sign in with GitHub**. A browser window will open to authorize VS Code.
5. Create a Local Folder For the Project
   - For Windows: navigate to the C drive, then go to Users, your username, and create a folder (e.g. `Projects`)
   - For Mac: open Finder, go to your home folder, and create a folder (e.g. `Projects`)
   - Remember where this folder is. You will choose it as the destination when cloning the repository.
6. Set up a ```.env``` file to hold any API keys used in the project as well as a ```.gitignore``` file. 
   - See the guide here [API key guide]("API_Key_Safety_And_Usage.md") for setup and more details on best practices and what to do if something goes wrong!
  
### GitHub Basics
**Introduction to GitHub:** GitHub is an important version control tool based on Git that helps single developers all the way up to large teams cleanly and safely work on projects. The most important feature is that it tracks all changes made over time. This is really helpful when dealing with a codebase that can be changed by many people over time. The following describe the different elements and fuctionalites you will need to use.
1. **Repositories**
   - This entire project exists in a *Repository.* Think of this like a folder on your computer. You can add folders and files to the repository throughout development.
2. **Branches**
    - The *Main Branch* is the public-facing branch of the project and is the base of the project for all team members. It is the expected practice to not publish your changes directly to this branch.
    - *Creating Your Own Branch:* Each developer on the project will create their own branch. While you are still in the development and debugging process, you will push all your updates here. When you are sure that your work is ready, you can *merge* your branch with the *main branch* and this will be approved by the owner or designated team members. 
      - Steps to create your own branch in VS Code:- Navigate to the option described in the image below
        - Once there, it will give you the option to name the branch, give it a name that identifies that it is yours.
       - Press Enter. VS Code creates the branch and switches to it automatically. You can confirm by checking the branch name in the bottom-left corner of VS Code.
  ![alt text](image.png)
      - *Switching Branches:* Click the branch name in the bottom-left corner and select another branch from the list. Always check which branch you are on before you start making changes.
3. **Commits**
   - A *commit* is a saved snapshot of your changes. Each commit has a short message describing what you changed and why.
   - Steps to make a commit in VS Code:
     - Open the *Source Control* panel in the left sidebar. It lists every file you have changed.
     - Click the **+** next to a file to *stage* it (or stage all changes at once).
     - Type a short, clear message in the message box (e.g. "Add login form validation").
     - Click **Commit**.
   - Commit small and often. Small commits are easier to review and easier to undo.
4. **Pushing and Pulling**
   - *Push* uploads your local commits to GitHub. The first time you push a new branch, click **Publish Branch**. After that, click **Sync Changes**.
   - *Pull* downloads the latest changes from GitHub to your computer. Pull before you start working each day so you are not building on outdated code.
5. **Pull Requests**
   - A *Pull Request (PR)* is how you ask to merge your branch into the main branch. It lets the team review your work before it becomes part of the project.
   - Steps to open a pull request:
     - Push your branch to GitHub.
     - On the repository page, click **Compare & pull request**.
     - Confirm the *base* branch is `main` and the *compare* branch is yours.
     - Add a title and a short description of what changed and why.
     - Click **Create pull request**.
   - A reviewer (the owner or a designated team member) will comment, request changes, or approve. If changes are requested, commit them to the same branch and the PR updates automatically.
6. **Merging**
   - Once the PR is approved, click **Merge pull request** on GitHub. Your changes are now part of the main branch.
   - After merging, switch back to `main` and pull the latest changes so your computer matches GitHub:
     - Click the branch name in the bottom-left and select `main`.
     - Click **Sync Changes** (or run `git pull`).
   - You can delete your old branch after merging and create a fresh one for your next task.
7. **Merge Conflicts**
   - A *merge conflict* happens when two people change the same lines of a file. Git cannot decide which version to keep, so you have to choose.
   - VS Code highlights the conflict and offers **Accept Current Change**, **Accept Incoming Change**, or **Accept Both Changes**. Pick the right option, save the file, then commit.
   - Pulling often and keeping branches short-lived makes conflicts much less common.

**Recommended Workflow Summary**
1. Pull the latest `main`.
2. Create your own branch.
3. Make changes and commit often.
4. Push (publish) your branch.
5. Open a pull request.
6. Get it reviewed and approved.
7. Merge, then switch back to `main` and pull.

### Cloning the Repository

**What is cloning?** Cloning downloads a full copy of a GitHub repository (all files and the complete history) to your computer so you can work on it locally. You only need to do this once per device.

**Repository used in this guide:** [RPI-Faculty----Agentic-Search](https://github.com/milazz27/RPI-Faculty----Agentic-Search)

**Before you start**
- Install [Git](https://git-scm.com/downloads). To check if you already have it, open a terminal and run `git --version`.
- Install [Visual Studio Code](https://code.visualstudio.com/).
- Because this is a *public* repository, you can clone it without signing in. You will only need to sign in to GitHub later when you push your own changes.

**Option 1: Clone using VS Code (recommended)**
1. Open VS Code.
2. Open the Command Palette with `Ctrl+Shift+P` (`Cmd+Shift+P` on Mac).
3. Type **Git: Clone** and press Enter.
4. Paste the repository URL and press Enter: https://github.com/milazz27/RPI-Faculty----Agentic-Search.git
5. Choose the folder on your computer where the project should be saved (for example, a `Projects` folder).
6. When VS Code asks "Would you like to open the cloned repository?", click **Open**.
7. Confirm it worked: the project files should appear in the *Explorer* panel on the left, and the branch name `main` should appear in the bottom-left corner.

**Option 2: Clone using the terminal**
1. Open a terminal and navigate to the folder where you want the project:
```bash
   cd path/to/your/projects
```
2. Run:
```bash
   git clone https://github.com/milazz27/RPI-Faculty----Agentic-Search.git
```
3. Move into the project and open it in VS Code:
```bash
   cd RPI-Faculty----Agentic-Search
   code .
```

**Where to find the clone URL on GitHub**
1. Go to the repository page.
2. Click the green **Code** button.
3. Under the **HTTPS** tab, click the copy icon next to the URL.

**After cloning**
- You are on the `main` branch. **Do not make changes directly on `main`.**
- Create your own branch before editing anything (see the *Branches* section above).
- Pull regularly to stay up to date with the team's changes.

**Troubleshooting**
- *"git is not recognized" / "git not found":* Git is not installed or VS Code needs a restart after installing it.
- *Clone fails or hangs:* Check your internet connection and make sure the URL was copied completely, including the repository name's multiple dashes (`RPI-Faculty----Agentic-Search`).
- *Folder already exists:* Choose a different destination folder or rename the existing one.