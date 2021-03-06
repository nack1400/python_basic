import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = f"https://search.indeed.jobs/main/jobs?keywords=python&location=&limit={LIMIT}&page=1"


def get_last_page():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser")

    pagination = soup.find("div", {"class": "pagination"})

    links = pagination.find_all('a')
    pages = []
    for link in links:
        pages.append(int(link.string))

    max_page = pages[-1]
    return max_page


def extract_job(html):
    title = html.find("div", {"class": "title"}).find("a")["title"]
    company = html.find("span", {"class": "company"})
    if company:
      if company.find("a") is not None:
          company = str(company.find("a").string)
      else:
          company = str(company.string)
    else:
      company = None
    company = company.strip()
    location = html.find("span", {"class": "recJobLoc"})["data-rc-loc"]
    job_id = html["data-jk"]
    return {
        'title': title,
        'company': company, 
        'location': location, 
        "link": f"https://www.indeed.com/viewjob?jk={job_id}"
    }


def extract_jobs(last_page):
    jobs = []
    for page in range(last_page):
        print(f"Scrapping SO: page: {page}")
        result = requests.get(f"{URL}&start={page*LIMIT}")
        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find_all("div", {"class": "jobsearch-SerpJobCard"})
        for result in results:
            job = extract_job(result)
            jobs.append(job)
    return jobs

def get_jobs():
  last_page = get_last_page()
  jobs = extract_jobs(last_page)
  return jobs