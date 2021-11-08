from bs4 import BeautifulSoup
import requests 
import pandas as pd 

URL ='https://en.wikipedia.org/wiki/Wikipedia:Top_25_Report/October_17_to_23,_2021'
response = requests.get(URL)
soup = BeautifulSoup(response.text, 'html.parser')

print(soup)
