################### BOT ###########
import requests
from bs4 import BeautifulSoup
import time 
import datetime
#from create_table import create_tables
#import psycopg2


x = 1
d = 1

for j in range (1000):
  while x == 1:
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
    
    while d == 1:
      ###############################################################connect to database and create table
      #create_table.run()
      d += 1
      ##########################################################################
  
    data = []
  
    for x in range(1, 11):
      row = html_data.find_all('tr')[x]
      column_value = row.find_all('td')
      dict = {}
          
      for i in range(6):
        dict[headings_list[i]] = column_value[i].text
      data.append(dict)
    
    crypto.write(data)
    
    for coin in data: 
      d = str(coin)
      n = str(now)
      #################################################################### connect to database
      #conn=psycopg2.connect("dbname=ddt3jth60iul84, user=lmhhwkksgpwqbs, password=bfc5d49a5575e869e5a39f3cc9d9bc79585a283dfa5189b6fa37a0d30ed6e11d, host=ec2-54-157-160-218.compute-1.amazonaws.com, port=5432")
      #################################################################### add values to table (broken)
      #db = INSERT INTO coin (now, heading_list) VALUES (n, d) #invalid syntax
      #conn.cursor.execute(db)
      ##############################################################################
      crypto.write(n) [remove]
      crypto.write(d) [remove]
      ##########################################################################close database
      #cursor.close()
      #conn.commit()
      #conn.close()
      ##########################################################################
      print(n+""+d)
      print('')
    crypto.close() [remove]
  time.sleep(10)   #(3600)
  x=1
#################################
