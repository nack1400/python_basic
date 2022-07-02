from reprlib import recursive_repr
from sys import last_type
import requests
from bs4 import BeautifulSoup

URL = f"https://stackoverflow.com/jobs/companies?q=python"


def get_last_page():
    result = requests.get(URL)
    soup = BeautifulSoup(soup.text, "html.parser")
    pages = soup.find("div", {"class": "pagination"}).find_all("a")
    last_page = pages[-2].get_text(strip=True)
    return last_page


def extract_job(html):
    title = html.find("div", {"class": "-title"}).find("h2").find("a")["title"]
    company, location = html.find(
        "div", {"class": "-company"}).find_all("span", recursive=False)
    print(company.get_text(strip=True), location.get_text(strip=True))
    return {"title": title}


def extract_jobs(last_page):
    jobs = []
    for page in range(last_page):
        result = requests.get(f"{URL}&pg={page+1}")
        soup = BeautifulSoup(result.text, "html.parser")
        result = soup.ffind_all("div", {"class": "-job"})
        for result in results:
            print(result["data-jobid"])


def get_jobs():
    last_page = get_last_page()
    return []
