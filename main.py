import requests
from bs4 import BeautifulSoup

indeed_result = requests.get(
    "https://search.indeed.jobs/main/jobs?keywords=python&location=&limit=50&page=1")

indeed_soup = BeautifulSoup(indeed_result.text, "html.parser")

pagination = indeed_soup.find("div", {"class": "pagination"})

links = pagination.find_all('a')
pages = []
for link in links:
    pages.append(int(link.string))

max_page = pages[-1]
print(pages)
