################### BOT ###########
import requests
from bs4 import BeautifulSoup
import time 
import datetime


x=1

for j in range (1000):
  while(x==1):
    crypto = open("crypto.json", "a")
    now = datetime.datetime.now()
        
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
      execute_query(connection,n,d)
      #crypto.write(n)
      #crypto.write(d)
      print(coin)
      print('')
    crypto.close()
  time.sleep(10)
  x=1
#################################
