from datetime import datetime
import time
from cassandra.cluster import Cluster
from cassandra.query import SimpleStatement, BatchStatement
from cassandra.policies import DCAwareRoundRobinPolicy
from cassandra.auth import PlainTextAuthProvider

from cassandra.cluster import ExecutionProfile, EXEC_PROFILE_DEFAULT
from cassandra.policies import WhiteListRoundRobinPolicy
from cassandra.query import tuple_factory
import pika
import os
import re

##
## Configure test vs. production
##


#cluster = Cluster()
cluster = Cluster(['127.0.0.1'],port=9042)


def insert_customer(customer_data):
  try:
    session = cluster.connect('test1')
    username = customer_data['username']
    email = customer_data['email']
    password = customer_data['password']
    print(username, email , password)

    stmt = session.prepare('INSERT INTO customer (username,email,password) '
                            'VALUES (?, ?, ?)'
                           'IF NOT EXISTS')
    results = session.execute(stmt, [ customer_data['username'], customer_data['email'], customer_data['password'] ])
    print("done session")
  
  
  except Exception as e:
    enqueueDataToLogsExchange("Exception occured" + str(e),"debug")
    print("Exception occured" + str(e))
  
  return customer_data


def search_customer(customer_data):
  try:
   
    session = cluster.connect('test1')
    print(customer_data)

    msg =''
    email = customer_data['username']
    #email = customer_data['email']
    password = customer_data['password']
    print(email , password)
    query = "select * from customer where email='"+ email + "' and password='" + password+ "' ALLOW FILTERING;"
    print(query)

    rows = session.execute(query)
    print(type(rows))
    c = 0
    for i in rows:
        c+=1
    print(c)



    print("done session")

      # If account exists in accounts table in out database
    if c > 0:
        print("done resultset")
        print("Logged in successfully!")
        return customer_data
    else:
            # Account doesnt exist or username/password incorrect
         msg = 'Incorrect username/password!'
         print(msg)
         return msg
         
  
  except Exception as e:
    #enqueueDataToLogsExchange("Exception occured" + str(e),"debug")
    print("Exception occured" + str(e))
  
 




def presentindatabase(search_term):
    try:
      results = {}
      session = cluster.connect('test1')
      # rows = session.execute("SELECT * FROM products.products WHERE productname LIKE '" + search_term + "%' ALLOW FILTERING;")
      rows = session.execute("SELECT * FROM products.products;")
      if(rows):
        for i in rows:
          print("Item")
          print(i)
          if search_term.lower() in i[2].lower():
            if(i[4] in results):
              results[i[4]].append({
                "productname": i[2],
                "productprice": i[3],
                "website":i[4],
                "product_url":i[5],
                "product_image_url":i[6]
              })

            else:
              results[i[4]] = []
              results[i[4]].append({
                "productname": i[2],
                "productprice": i[3],
                "website":i[4],
                "product_url":i[5],
                "product_image_url":i[6]
              })
        
      return results
    except Exception as e:
      enqueueDataToLogsExchange("Exception occured" + str(e),"debug")
      print("Exception occured" + str(e))


