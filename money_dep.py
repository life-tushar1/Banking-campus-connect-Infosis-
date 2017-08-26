import pymysql
import sys
from time import gmtime, strftime
class money_dep:
    def money_deposit(self,cus):
           conn2=pymysql.connect("localhost","root","","bankM5",autocommit=True)
           cur2=conn2.cursor()
           print("enter which account:")
           acc=raw_input()
           acc=str(acc)
           sq3="SELECT acc_type from account_type where cust_id= "+cus+" and acc_type='"+acc+"'"
           t=cur2.execute(sq3)
           if(t==1):
                showtime = strftime("%Y-%m-%d %H:%M:%S", gmtime())
                print"enter amount to deposit: "
                dep=raw_input()
                dep=int(dep)
                sql1="select min_balance from account_type where cust_id= "+cus+" and acc_type ='saving'"
                cur2.execute(sql1)
                v=cur2.fetchone()
                v1=v[0]
                v1=int(v1)
                final=v1+dep
                final=str(final)
                dep=str(dep)
                sql1="update account_type set min_balance ='"+final+"' where cust_id="+cus+" and acc_type='"+acc+"'"
                sql2="insert into transact values('"+cus+"','"+acc+"','"+showtime+"','"+final+"','"+dep+"','0',null,null)"
                #print sql2
                cur2.execute(sql1)
                cur2.execute(sql2)


    
