# the needed imports 
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
# gets the url and finds the values
que = input("search the 5e wiki")
testTia = 'https://www.dandwiki.com/wiki/5e_SRD:' + que
page = requests.get(testTia)
soup = bs(page.content,'html.parser')

#gets and prints the name
name = soup.find('h2')
print(name.string)

#gets the trait aspect
desc = soup.find_all('p')
print(desc[1].string); 

traits = soup.find_all('i')
print(traits[2].string); 
traits1 = soup.find_all('i')
print(traits1[3].string); 
traits2 = soup.find_all('i')
print(traits2[4].string); 
traits3 = soup.find_all('i')
print(traits3[5].string)
 # works for taking in traits