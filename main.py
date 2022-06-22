import requests
from bs4 import BeautifulSoup

indeed_result= requests.get("https://search.indeed.jobs/main/jobs?keywords=python&location=&limit=50&page=1")

indeed_soup = BeautifulSoup(indeed_result.text, "html.parser")