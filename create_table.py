import psycopg2
from config import config
  
  
def create_tables():
   
    commands = ("""CREATE TABLE coin (now,heading_listing)""")
    # connect to the PostgreSQL server
    conn = psycopg2.connect("dbname=ddt3jth60iul84, user=lmhhwkksgpwqbs, password=bfc5d49a5575e869e5a39f3cc9d9bc79585a283dfa5189b6fa37a0d30ed6e11d, host=ec2-54-157-160-218.compute-1.amazonaws.com, port=5432")
    cur = conn.cursor()
    # create table one by one
    for command in commands:
      cur.execute(command)
      # close communication with the PostgreSQL database server
      cur.close()
      # commit the changes
      conn.commit()
      if conn is not None:
        conn.close()

if __name__ == '__main__':
    create_tables()
