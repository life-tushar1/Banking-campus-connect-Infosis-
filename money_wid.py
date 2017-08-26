import pymysql
import sys
from time import gmtime, strftime
class money_wid:
    def money_withdrawl(self,cus):
           #query to withdraw money
           conn2=pymysql.connect("localhost","root","","bankM5",autocommit=True)
           cur2=conn2.cursor()
           print("enter which account:")
           acc=raw_input()
           acc=str(acc)
           sq3="SELECT acc_type from account_type where cust_id= "+cus+" and acc_type='"+acc+"'"
           t=cur2.execute(sq3)
           if(t==1):
               if(acc=="saving"):
                   print("enter amount to wid:")
                   wid=raw_input()
                   wid=int(wid)
                   sql1="select min_balance from account_type where cust_id= "+cus+" and acc_type ='saving'"
                   cur2.execute(sql1)
                   v=cur2.fetchone()
                   v1=v[0]
                   v1=int(v1)
                   final=v1-wid
                   if(final<0):
                        print"cannot withdraw due to low balance rolling back....."
                   else:
                       showtime = strftime("%Y-%m-%d %H:%M:%S", gmtime())
                       final=str(final)
                       wid=str(wid)
                       sql1="update account_type set min_balance ='"+final+"' where cust_id="+cus+" and acc_type='saving'"
                       sql2="insert into transact values('"+cus+"','saving','"+showtime+"','"+final+"','0','"+wid+"',null,null)"
                       cur2.execute(sql1)
                       cur2.execute(sql2)
               else:
                   print("enter amount to wid:")
                   wid=raw_input()
                   wid=int(wid)
                   sql1="select min_balance from account_type where cust_id= "+cus+" and acc_type ='current'"
                   cur2.execute(sql1)
                   v=cur2.fetchone()
                   v1=v[0]
                   v1=int(v1)
                   final=v1-wid
                   if(final<5000):
                        print"cannot withdraw due to low balance rolling back....."
                   else:
                       showtime = strftime("%Y-%m-%d %H:%M:%S", gmtime())
                       final=str(final)
                       wid=str(wid)
                       sql1="update account_type set min_balance ='"+final+"' where cust_id="+cus+" and acc_type='current'"
                       sql2="insert into transact values('"+cus+"','current','"+showtime+"','"+final+"','0','"+wid+"',null,null)"
                       cur2.execute(sql1)
                       cur2.execute(sql2)
           else:
            print"exiting"
            
                   
           
    