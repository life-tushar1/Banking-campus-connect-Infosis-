import pymysql
class loan_wrt:
        def wrt(self):
                    conn=pymysql.connect("localhost","root","","bankM5",autocommit=True)
                    cur=conn.cursor()
                    amount=raw_input("enter n amount of 1000 notes ")
                    amount=int(amount)
                    if(amount<1):
                        print "invalid entry"
                    else:
                        amount=amount*1000
                        amount=str(amount)
                        print"*****************************************"
                        print"|cust_id| first_name | last name |amount|"
                        print"*****************************************"
                        sql="select cust_id,loan_amt from loan where loan_amt >"+amount
                        t=cur.execute(sql)
                        #t1=cur.fetchall()
                        #print t
                        #print t1
                        if(t>=1):
                            #print "reached"
                            result=cur.fetchall()
                            #print result
                            for row in result:
    
                                #print row[0]
                                row1=str(row[0])
                                sql="select first_name,last_name from cust_info where cust_id="+row1
                                cur.execute(sql)
                                t=cur.fetchall()
                                for name in t:
                                       q=str(name[0])
                                       q1=str(name[1])
                                       q3=str(row[1])
                                       print"|"+row1+"      |"+q+"     |"+q1+"     |"+q3+"  | "
    

                        print"******************************************"


