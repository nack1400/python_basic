import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = f"https://search.indeed.jobs/main/jobs?keywords=python&location=&limit={LIMIT}&page=1"

def extract_indeed_pages():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser")

    pagination = soup.find("div", {"class": "pagination"})

    links = pagination.find_all('a')
    pages = []
    for link in links:
        pages.append(int(link.string))

    max_page = pages[-1]
    return max_page

def extract_indeed_jobs(last_page):
  jobs = []
  # for page in range(last_page):
  result = requests.get(f"{URL}&start={page*LIMIT}")
  soup = BeautifulSoup(result.text, "html.parser")
  results = soup.find_all("div", {"class": "jobsearch-SerpJobCard"})
  for result in results:
    title = result.find("div", {"class": "title"}).find("a")["title"]
  return jobs