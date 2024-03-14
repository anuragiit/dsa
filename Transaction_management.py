import cx_Oracle
class AccDoesNotExist(Exception):
    pass
con=None
try:
   con=cx_Oracle.connect('anurag','anuragiit','localhost:1521/orcl')
   cur=con.cursor()
   print("Initial balance details")
   cur.execute("select * from cust_acc_bal")
   for row in cur:
         print(row)
   ac1=input("Enter account from which u want to deduct balance")
   ac2=input("Enter account to which u want to transfer balance")
   transfer_amt=input("Enter amount to be transferred ")
   query1="update cust_acc_bal set balance=balance-"+transfer_amt+"where id="+ac1
   cur.execute(query1)
   if cur.rowcount!=1:  #value of rowcount attribute is calculated wrt no of manipulations done in single query
       print("Account No of donor doesnot Exist")
       raise AccDoesNotExist
   
   query2="update cust_acc_bal set balance=balance+"+transfer_amt+"where id="+ac2
   cur.execute(query2)
  
   if cur.rowcount!=1:
       print("Account No of receiver doesnot Exist")
       raise AccDoesNotExist
    
   print("Transaction successful")
except(AccDoesNotExist):
    con.rollback()
    print("Transaction Failed")
except(cx_Oracle.DatabaseError):
    print("Couldn't connect to database")
    
except:
    print("Error Occured somewhere!!Try again")
finally:
    print("Balance details after transaction")
    cur.execute("select * from cust_acc_bal")
    for row in cur:
         print(row)
      
    if con!=None:
        cur.close()
        con.commit()
        
        con.close()
     
       
   
 
