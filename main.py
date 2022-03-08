################### BOT ###########
import requests
from bs4 import BeautifulSoup
import time 
import datetime

#import psycopg2

x=1
#d=1

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
    
    #while d=1:
      ###############################################################connect to database
      #conn=psycopg2.connect("databasename=? user=? password=?")
      #CREATE TABLE coin(headings_list)
      #d +=1
      ##########################################################################close database
      #conn.close()
      ##########################################################################
  
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
      #################################################################### connect to data base
      #conn=psycopg2.connect("databasename=? user=? password=?")
      #################################################################### add values to table
      #data="INSERT INTO coin_table(heading_list) VALUES (n,d)"
      #conn.cursor.execute(data)
      ######crypto.write(n) [remove]
      ######crypto.write(d) [remove]
      ##########################################################################close database
      #cursor.close()
      #conn.commit()
      #conn.close()
      ##########################################################################
      print(coin)
      print('')
    #crypto.close() [remove]
  time.sleep(3600)
  x=1
#################################
