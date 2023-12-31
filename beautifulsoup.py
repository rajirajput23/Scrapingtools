import requests
from bs4 import BeautifulSoup
import html5lib
import csv

#  URL OF THE WEBSITE WE WANT TO SCRAPE
url="http://www.values.com/inspirational-quotes"
responce=requests.get(url)

#CREATING A BEAUTIFULSOUP OBJECT
soup=BeautifulSoup(responce.content,"html5lib")
print(soup.prettify())

quotes=[]  # a list to store quotes
   
table = soup.find('div', attrs = {'id':'all_quotes'}) 
   
for row in table.find_all_next('div',
        attrs = {'class':'col-6 col-lg-3 text-center margin-30px-bottom sm-margin-30px-top'}):
    quote = {}
    quote['theme'] = row.h5.text
    quote['url'] = row.a['href']
    quote['img'] = row.img['src']
    quote['lines'] = row.img['alt'].split(" #")[0]
    quote['author'] = row.img['alt'].split(" #")[1]
    quotes.append(quote)

print(table.prettify())

filename = 'inspirational_quotes.csv'
with open(filename, 'w', newline='') as f:
    w = csv.DictWriter(f,['theme','url','img','lines','author'])
    w.writeheader()
    for quote in quotes:
        w.writerow(quote)