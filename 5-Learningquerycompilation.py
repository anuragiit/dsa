import cx_Oracle
import datetime           # we have to import datetime module for passing dates or dates with times
con=cx_Oracle.connect("anurag",'anuragiit','localhost:1521/orcl')
cur=con.cursor()
cur.arraysize=100
cur.prepare("select * from miningmarks where rollno =:r")
cur.execute(None,r=15155015)
cur.prepare("select rollno,name from miningmarks where rollno =:r")
cur.execute(None,{'r':15155015})
for rec in cur:
    print(rec)
cur.execute(None,r=15155018)    
cur2=con.cursor()
cur2.arraysize=100
cur2.prepare("Insert into miningmarks values (:a,:b,:c,:d)")
cur2.execute(None,a=15155005,b='Abhishek',c=79,d=datetime.date(1996,10,28))
recs=[(15155041,"Ashraf",96,datetime.date(1996,9,21)),(15155050,"Pratik",88,datetime.date(1996,7,25))]
cur3=con.cursor()
cur3.arraysize=100
cur3.executemany("insert into miningmarks values(:a,:b,:c,:d)",recs)
cur3.execute("select * from miningmarks")
for row in cur3.fetchall():
    print(row)
  
#con.commit()        #this statement is commented so that program can run many time as rollno is primary key    
cur2.close()
cur.close()
cur3.close()
con.close()

