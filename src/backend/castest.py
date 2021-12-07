import logging

log = logging.getLogger()
log.setLevel('INFO')
#handler = logging.StreamHandler()
#handler.setFormatter(logging.Formatter("%(asctime)s [%(levelname)s] %(name)s: %(message)s"))
#log.addHandler(handler)
from datetime import datetime
import time
from cassandra.cluster import Cluster
from cassandra.query import SimpleStatement, BatchStatement
if __name__ == "__main__":
    cluster = Cluster(['127.0.0.1'],port=9042)
    session = cluster.connect('test1',wait_for_all_pools=True)
    session.execute('USE test1')
    #rows = session.execute('SELECT * FROM cities')
    #insert_sql = ("INSERT INTO cities (id,name,country) "
              #"VALUES(%d, %s, %s) ")
    #insert_data = (int(6), 'Arp', 'India')


    #stmt = session.prepare('INSERT INTO activate (id,insert_time,qualifier) '
                            #'VALUES (?, ?, ?)'
                           #'IF NOT EXISTS')
    #results = session.execute(stmt, [arg1, arg2, ...])
    

    #timestamp = int(time.time())

    
    now = datetime.utcnow()
    #rows = session.execute(stmt, [6,now,'Arpita'])

    
    #add sleep command for 5secs
    #time.sleep(5)

    #rows = session.execute('SELECT * FROM activate')
    #for row in rows:
        #print(row.id,row.insert_time,row.qualifier)
    #log.info("original time: %s", now)

    studentlist={'username': 'arpita_ambavane', 'email': 'arpita.ambavane@colorado.edu', 'password': 'jnjbjbj'}
    print(studentlist.username);

    rows = session.execute("INSERT INTO customer (username, email ,password) VALUES ( {0}, {1}, {2} );")

     

    #batch=BatchStatement()
    #for student in studentlist:
        #batch.add(SimpleStatement("INSERT INTO customer (user_name, email_id, pwd) VALUES(%s, %s, %s)"), (student[0], student[1],student[2]))
    #session.execute(batch)

    #how to deploy cassandra like redis.yaml file container to other containers

    #Data sent by Shefali will be: Customer email , customerName, timestamp, expense values, expense category 
    





   
