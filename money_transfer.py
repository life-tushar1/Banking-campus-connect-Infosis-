import pymysql
import sys
from time import gmtime, strftime
class money_transfer:
    def tranfer(self,cus,cus2):
         conn2=pymysql.connect("localhost","root","","bankM5",autocommit=True)
         cur2=conn2.cursor()
         print"enter the account from which u want to transfer from "
         acc=raw_input()
         acc=str(acc)
         acc=str(acc)
         sq3="SELECT acc_type from account_type where cust_id= "+cus+" and acc_type='"+acc+"'"
         t=cur2.execute(sq3)
         showtime = strftime("%Y-%m-%d %H:%M:%S", gmtime())
         if(t==1):
             sq3="SELECT acc_type from account_type where cust_id= "+cus2+" and acc_type='"+acc+"'"
             t1=cur2.execute(sq3)
             if(t1==1):
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
                       
                       sq1="select min_balance from account_type where cust_id= "+cus2+" and acc_type ='saving'"
                       cur2.execute(sql1)
                       v=cur2.fetchone()
                       v1=v[0]
                       v1=int(v1)
                       final1=v1+wid
                       final1=str(final1)
                       
                       
                       
                       final=str(final)
                       wid=str(wid)
                       sql3="update account_type set min_balance = '"+final1+"' where cust_id="+cus2+" and acc_type='saving'"
                       sql1="update account_type set min_balance ='"+final+"' where cust_id="+cus+" and acc_type='saving'"
                       sql2="insert into transact values('"+cus+"','saving','"+showtime+"','"+final+"','0','"+wid+"','"+cus+"','"+cus2+"')"
                       sql4="insert into transact values('"+cus2+"','saving','"+showtime+"','"+final1+"','"+wid+"','0','"+cus+"','"+cus2+"')"
                       
                       cur2.execute(sql1)
                       cur2.execute(sql2)
                       cur2.execute(sql3)
                       cur2.execute(sql4)
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
                       sq1="select min_balance from account_type where cust_id= "+cus2+" and acc_type ='current'"
                       cur2.execute(sql1)
                       v=cur2.fetchone()
                       v1=v[0]
                       v1=int(v1)
                       final1=v1+wid
                       final1=str(final1)
                       
                       
                       
                       final=str(final)
                       wid=str(wid)
                       sql3="update account_type set min_balance = '"+final1+"' where cust_id="+cus2+" and acc_type='current'"
                       sql1="update account_type set min_balance ='"+final+"' where cust_id="+cus+" and acc_type='current'"
                       sql2="insert into transact values('"+cus+"','"+acc+"','"+showtime+"','"+final+"','0','"+wid+"','"+cus+"','"+cus2+"')"
                       sql4="insert into transact values('"+cus2+"','"+acc+"','"+showtime+"','"+final1+"','"+wid+"','0','"+cus+"','"+cus2+"')"
                       
                       cur2.execute(sql1)
                       cur2.execute(sql2)
                       cur2.execute(sql3)
                       cur2.execute(sql4)
             else:
                print"other id account does exist plz try again"