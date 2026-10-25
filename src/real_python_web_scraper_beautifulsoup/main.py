import requests
from bs4 import BeautifulSoup

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

result = soup.find(id="ResultsContainer")

python_jobs = result.find_all('h2', string=lambda text: "python" in text.lower())
python_job_cards = [h2.parent.parent.parent for h2 in python_jobs]
    
for job in python_job_cards:
    title = job.find("h2", class_='title')
    company = job.find('h3', class_='company')
    location = job.find('p', class_='location')
    print(title.text.strip(), company.text.strip(), location.text.strip(), sep='\n', end='\n\n')

