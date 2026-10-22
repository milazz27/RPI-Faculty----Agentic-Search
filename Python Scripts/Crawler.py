"""
This file contains code related to the base functionality of the crawler at the base of the program.
It begins from a base URL and collects the department-specific links to crawl for faculty listing. From this point
it will visit each faculty page and invoke code to scrape the relevant information and continue onto the next.
"""

from bs4 import BeautifulSoup
import requests

def department_page_extract(page):
    pass

def base_crawl(url="https://faculty.rpi.edu/departments"):
    '''
    @brief: central crawling function for project; controls all crawling branches.

    @param: url: base url for crawling, defaults to department page.
    @return: True when execution terminates successfully.
    '''

    # Initiate the crawl by grabbing base page
    try:
        page = requests.get(url)
        soup = BeautifulSoup(page.text, "html.parser")
    except Exception as e:
        print("Error requesting base url: {e}")
        return False #flag for unexpected termination of the function

    # Save result to output file:
    base_html = "base_page.html"
    with open(base_html, "w", encoding="utf-8") as f:
        f.write(soup.prettify())

    print("Saved to {base_html}")

if __name__ == "__main__":
    base_crawl()