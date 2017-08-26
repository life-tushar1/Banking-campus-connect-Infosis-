import pymysql
import sys
from database_entry import database_entry
class sign_in:
    def signin_info(self):
        conn=pymysql.connect("localhost","root","","bankM5",autocommit=True)
        cur=conn.cursor()
        sq3="SELECT * FROM cust_info"
        cur.execute(sq3)
        r=cur.rowcount+1
        r=r-1
        var2=1
        while var2==1:
            invalid_count=0
            print("enter your existing customer id")
            ex_id=raw_input()
            if(ex_id.isdigit()):
            
             ex_id=int(ex_id)
            
             if(ex_id>r or ex_id<1):
                print("invalid id")
                sys.exit(0)
             else:
                ex_id=str(ex_id)
                
                sqlb="select block from cust_info where cust_id = "+ex_id
                cur.execute(sqlb)
                checking=cur.fetchone()
                
                temp="('yes',)"
                checking=str(checking)
                if(checking == temp):
                        print("You are blocked contact the admin")
                        sys.exit(0)
                var3=1
                while var3 ==1:
                    if invalid_count == 3:
                        ex_id=str(ex_id)
                        print("You are blocked")
                        sql4="UPDATE cust_info SET Block = 'yes' WHERE cust_id= "+ex_id
                        cur.execute(sql4)
                        sys.exit(0) 
                        
                        
                    print("enter your existing password")
                    ex_pass=raw_input()
                    sql1="select password from login where cust_id = "+ex_id
                    cur.execute(sql1)
                    checking=cur.fetchone()
                
                    temp="('"+ex_pass+"',)"
                
                    checking=str(checking)
                 
                
                    if(checking == temp):
                        var2=2
                        var3=2
                        print("You are logged in")
                    else:
                        print("invalid")
                        invalid_count+=1
                        
       
        s1=database_entry()
        s1.entry(ex_id)
        
    
  
