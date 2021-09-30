import requests
from bs4 import BeautifulSoup
from urllib.parse import unquote

URL = 'https://arduboy.ried.cl/'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
hexLinks = soup.find_all('a', class_='style3')

for hexLink in hexLinks:
    link = hexLink['href']
    print(unquote(link.split('/')[-1]).replace('/','_'))
    r = requests.get(link)
    #with open(unquote(link.split('/')[-1]).replace('/','_'),'wb') as f:
    with open('hex/' + unquote(link.split('/')[-1]).replace('/','_'),'wb') as f:
        f.write(r.content)