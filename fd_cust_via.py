import pymysql
class fd_cust_via:
         def via(self):
                    conn=pymysql.connect("localhost","root","","bankM5",autocommit=True)
                    cur=conn.cursor()
                    sql2="select * from cust_info"
                    cur.execute(sql2)
                    r=cur.rowcount
                    print("enter cust_id:")
                    cus=int(raw_input())
                    
                    if(cus>r):
                        print"invalid id"
                    else:
                     cus=str(cus)
                     sql="select * from fd where cust_id="+cus
                     t=cur.execute(sql)
                     if(t==0):
                         print"fd account doesnt exist"
                     else:
                         result = cur.fetchall()
                         sum=0
                         for row in result:
                             sum=sum+row[1]
                         sum=str(sum)
                         sql2="select * from fd where  amount>="+sum+" and cust_id != "+cus
                         cur.execute(sql2)
                         result = cur.fetchall()
                         print"*******************************"
                         print"| acc_no| amount | duration  |"
                         print"*******************************"
                         for row in result:
                            s=str(row[2])
                            s1=str(row[1])
                            s2=str(row[0])
                            print"| "+s2+"      | "+s1+" | "+s+"      |"

                         print"*******************************"

        
