import requests
from bs4 import BeautifulSoup

indeed_result = requests.get(
    "https://search.indeed.jobs/main/jobs?keywords=python&location=&limit=50&page=1")

indeed_soup = BeautifulSoup(indeed_result.text, "html.parser")

pagination = indeed_soup.find("div", {"class": "pagination"})

pages = pagination.find_all('a')
spans = []
for page in pages:
    spans.append(page.find("span"))
print(spans[:-1])
