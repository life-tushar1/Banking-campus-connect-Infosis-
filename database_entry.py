import pymysql
import sys
from test import transPrint
from address import address
from money_dep import money_dep
from money_wid import money_wid
from acc_close import acc_close
from money_transfer import money_transfer
from open_new_acc import open_new_acc
from open_new_loan import open_new_loan
class database_entry:
    def entry(self,ex_id):
        var1 =1
        while var1 == 1:
          print "1 ADDRESS CHANGE"
          print "2 OPEN NEW ACCOUNT"
          print "3 MONEY DEPOSIT"
          print "4 MONEY WITHDRAWL"
          print "5 MONEY TRANSFER"
          print "6 PRINT STATEMENT"
          print "7 ACCOUNT CLOSURE"
          print "8 AVAIL LOAN"
          print "0 CUSTOMER LOGOUT"
          c=input()
          c=int(c)
          
          if c==1:
            s2=address()
            s2.add_change(ex_id)
          elif c==3:
              s2=money_dep()
              s2.money_deposit(ex_id)
          elif c==4:
              
              s2=money_wid()
              s2.money_withdrawl(ex_id)
          elif c==6:
              pr=transPrint()
              pr.printi(ex_id)
          elif c==5:
            
            s2=money_transfer()
            print("enter the id to transfer money")
            cus=raw_input()
            cus=int(cus)
            conn=pymysql.connect("localhost","root","","bankM5",autocommit=True)
            cur=conn.cursor()
            sq3="SELECT * FROM cust_info"
            cur.execute(sq3)
            r=cur.rowcount
            if(cus>r):
              print("wrong id plz input again:")
            else: 
              cus=str(cus)
              s2.tranfer(ex_id,cus)
          elif c==7:
            s2=acc_close()
            s2.account_closure(ex_id)
            var1=2
          elif c==0:
            print"logged out"
            var1=2
          elif c==2:
              
              s1=open_new_acc()
              s1.open(ex_id)
              
          elif c==8:
              
              s1=open_new_loan()
              s1.open(ex_id)
          elif c>8:
            print("wrong choice enter again")
   

         
