import requests
from bs4 import BeautifulSoup

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

result = soup.find(id="ResultsContainer")

job_cards = result.find_all("div", class_ = "card-content")

for job_card in job_cards:
    title_element = job_card.find("h2", class_ = "title")
    company_element = job_card.find("h3", class_ = "company")
    location_element = job_card.find("p", class_ = "location")
    print(title_element.text.strip(), company_element.text.strip(), location_element.text.strip(), sep='\n', end='\n\n')
    
