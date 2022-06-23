import requests
from bs4 import BeautifulSoup

indeed_result = requests.get(
    "https://search.indeed.jobs/main/jobs?keywords=python&location=&limit=50&page=1")

indeed_soup = BeautifulSoup(indeed_result.text, "html.parser")

pagination = indeed_soup.find("div", {"class": "pagination"})

links = pagination.find_all('a')
pages = []
for link in links[:-1]:
    pages.append(int(link.find("span")))

max_page = pages[-1]
