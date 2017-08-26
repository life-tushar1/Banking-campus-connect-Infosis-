import pymysql
class fd_report:
    def report(self):
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
                        print"this customer has no FD account"
                     else:
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
                        print ""
