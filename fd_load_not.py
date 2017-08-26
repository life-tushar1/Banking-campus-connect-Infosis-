import pymysql
class fd_loan_not:
         def noti(self):
                    conn=pymysql.connect("localhost","root","","bankM5",autocommit=True)
                    cur=conn.cursor()
                    sql2="select * from cust_info"
                    cur.execute(sql2)
                    r=cur.rowcount
                    listi=[]
                    for r in range(0,r+1):
                      listi.append(0)

                    sqlq="select cust_id from loan "
                    cur.execute(sqlq)
                    result=cur.fetchall()
                    for row in result:
                      r1=row[0]
                      listi[r1]+=1
                    sqlq="select cust_id from fd "
                    cur.execute(sqlq)
                    result=cur.fetchall()
                    for row in result:
                      r1=row[0]
                      listi[r1]+=1
                    print"**********************************"

                    print"| cust_id |first_name |last_name|"
                    print"**********************************"
                    for r in range(1,r+1):
                     if(listi[r]==0):
                      ids=r
                      ids=str(ids)
                      sql="select cust_id,first_name,last_name from cust_info where cust_id="+ids
                      cur.execute(sql)
                      re=cur.fetchall()
        
                      x=re[0]
                      aa=x[0]
                      aa=str(aa)
                      print("| "+aa+"       |"+x[1]+"     |"+x[2]+"     |") 

                    print"**********************************"
