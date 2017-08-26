import pymysql
class open_new_loan:
    def open(self,cus):
        print("enter the amount of notes of 1000 for loan:")
        loan=raw_input()
        loan=int(loan)
        loan=loan*1000
        conn=pymysql.connect("localhost","root","","bankM5",autocommit=True)
        cur=conn.cursor()
        sq3="SELECT * FROM loan"
        cur.execute(sq3)
        r=cur.rowcount+1
        
        sql="select min_balance from account_type where acc_type='saving' and cust_id='"+cus+"'"
        k=cur.execute(sql)
        if(k==0):
            print"ur not eligible for loan"
        else:
         v=cur.fetchone()
         v1=v[0]
         v1=int(v1)
         if(loan>(2*v1)):
            print"loan value exceeded try again and your loan value should be less or equal to 2x amount present in ur saving account"
         else:
            print"enter repay term in format yyyy-mm-dd "
            dat=raw_input()
            loan=str(loan)
            sql2="insert into loan values('','"+loan+"','"+dat+"','"+cus+"')"
            cur.execute(sql2)
            r=str(r)
            print "ur loan id is: "+r