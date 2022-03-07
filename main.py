
##################### BOT ###########
import requests
from bs4 import BeautifulSoup
import time 
from datetime import *



#while(x==1): #have loop run once every 60 mins
for j in range (1000):
  
  crypto = open("crypto.json", "a")
  now = datetime.now()
        
  url = 'https://coinmarketcap.com/'
  response = requests.get(url)
  text = response.text
  html_data = BeautifulSoup(text, 'html.parser')
  headings = html_data.find_all('tr')[0]
  headings_list = []
  for x in headings:
    headings_list.append(x.text)
  headings_list = headings_list[:6]
  #print (headings_list)
  
  data = []
  
  for x in range(1, 11):
    row = html_data.find_all('tr')[x]
    column_value = row.find_all('td')
    dict = {}
          
    for i in range(6):
      dict[headings_list[i]] = column_value[i].text
    data.append(dict)
          
  for coin in data: 
    d = str(coin)
    n = str(now)
    ###### write to database
    crypto.write(n)
    crypto.write(d)
    crypto.write("\n")
    print(coin)
    print('')
    time.sleep(10)
  crypto.close()
  #x=1
#################################
