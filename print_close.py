import pymysql
class print_close:
    def printi(self):
                    conn=pymysql.connect("localhost","root","","bankM5",autocommit=True)
                    cur=conn.cursor()
                    cur.execute("select * from cust_info where closed='yes'")
                    result = cur.fetchall()
                    print"****************************"
                    print"|customer id | close date |"
                    print"****************************"
                    for row in result:
                      s=row[2]
                      s=str(s)
                   
                      s1=row[10]
                      s1=str(s1)
                      print "| "+s+"          | "+ s1+" |"
                    print"****************************"
                    print("")

