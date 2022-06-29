import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = f"https://search.indeed.jobs/main/jobs?keywords=python&location=&limit={LIMIT}&page=1"
