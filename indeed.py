import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = f"https://kr.indeed.com/%EC%B7%A8%EC%97%85?q=python&limit={LIMIT}"

def extract_indeed_pages():
  result = requests.get(URL)

  soup = BeautifulSoup(result.text, 'html.parser')

  pagination = soup.find('div', {"class": "pagination"})

  links = pagination.find_all('a')

  pages = []
  for link in links[:-1]:
    pages.append(int(link.string))
  last_page = pages[-1]

  return last_page

def extract_indeed_jobs(last_page):
  jobs = []
  # for page in range(last_page):
  result = requests.get(f"{URL}&start={0*LIMIT}")
  soup = BeautifulSoup(result.text, 'html.parser')

  # title 추출
  results = soup.find_all("div", {"class": "jobsearch-SerpJobCard"})
  for res in results:
    title = res.find("div", {"class": "title"}).find("a")["title"]
    company = res.find("span", {"class": "company"})
    company_anchor = company.find("a")
    if company_anchor is not None:
      company = str(company.find("a").string)
    else:
      company = str(company.string)
    company = company.strip()
    print(f"title: {title}\ncompany: {company}\n")
  return jobs
