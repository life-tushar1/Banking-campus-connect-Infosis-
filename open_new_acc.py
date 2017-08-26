import pymysql
from time import gmtime, strftime
from __builtin__ import raw_input
from open_fb import open_fd
class open_new_acc:
    def open(self,cus):
        print "7.1 OPEN SA "
        print "7.2 OPEN CA"
        print "7.3 OPEN FD"
        x=raw_input()
        conn=pymysql.connect("localhost","root","","bankM5",autocommit=True)
        cur=conn.cursor()
        cur2=conn.cursor()
        showtime = strftime("%Y-%m-%d %H:%M:%S", gmtime())
        if x=="7.1":
            sq3="SELECT acc_type from account_type where cust_id= "+cus+" and acc_type='saving'"
            t=cur.execute(sq3)
            if(t==1):
                print("your saving account already exists")
            else:
                print("enter balance to deposit:")
                balance=raw_input()
                balance=int(balance)
                if(balance<0):
                    print("invalid amount")
                else:
                 balance=str(balance)
                 sql="update cust_info set balance ='0' where cust_id = "+cus
                 cur.execute(sql)
                 sql2="insert into account_type values('saving','"+balance+"','5','"+cus+"')"
                 sql3="insert into transact values('"+cus+"','saving','"+showtime+"','"+balance+"','"+balance+"','0',null,null)"
                
                 cur.execute(sql2)
                 cur.execute(sql3)
                 print("Saving account created")
        elif x=="7.2":
            sq3="SELECT acc_type from account_type where cust_id= "+cus+" and acc_type='current'"
            t=cur.execute(sq3)
            if(t==1):
                print("your current  account already exists")
            else: 
                print("enter balance to deposit:")
                balance=raw_input()
                balance=int(balance)
                if(balance<5000):
                    print("invalid amount")
                else:
                 balance=str(balance)
                 sql="update cust_info set balance ='0' where cust_id = "+cus
                 cur.execute(sql)
                 sql2="insert into account_type values('current','"+balance+"','5','"+cus+"')"
                 sql3="insert into transact values('"+cus+"','current','"+showtime+"','"+balance+"','"+balance+"','0',null,null)"
                
                 cur.execute(sql2)
                 cur.execute(sql3)
                 print("current account created")
        elif x=="7.3":
            
            s1=open_fd()
            s1.regist(cus)
        else:
            print "invalid input"
            