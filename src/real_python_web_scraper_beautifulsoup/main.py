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
    link = job.find_all('a')[1]['href']
    print(title.text.strip(), company.text.strip(), location.text.strip(), link, sep='\n') 

    sub_page = requests.get(link)
    sub_soup = BeautifulSoup(sub_page.content, 'html.parser')
    content = sub_soup.find('div', class_='content')
    print(content.find('p').text.strip(), end='\n\n')

