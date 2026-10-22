from bs4 import BeautifulSoup
import requests
import pandas as pd

"""
Helpful Tutorial: "https://www.youtube.com/watch?v=QhD015WUMxE"
"""

# Saving the base URL for where we want our program to scrape from
base_url = "https://quotes.toscrape.com/"

# Attempting to reach the page and grab the HTML text
try:
    page = requests.get(base_url)
    soup = BeautifulSoup(page.text, "html.parser")
except Exception as e:
    print("Error trying to reach page: {e}")

# Use the find_all function from Beautifull soup to grab all text from desired tags
# you can identify the tags you want to search for by inspecting the desired web page
quotes = soup.find_all("span", class_="text")
authors = soup.find_all("small", class_="author")

"""
# Inspect the results
for ele in zip(quotes, authors):
    print("in loop")
    print(ele[0].text, "\n", ele[1].text, end="\n\n")
"""

# Optional Next Step: Save to a pandas DataFrame
data = {"Author": authors, "Quote": quotes}
df = pd.DataFrame(data)

print(df.head())