import cx_Oracle
con=cx_Oracle.connect("scott","tiger","localhost:1521/orcl")
cur=con.cursor()
cur.execute("select empno,ename,sal from emp order by sal")
for rec in cur:
    print(rec)
cur.close()
con.close()
