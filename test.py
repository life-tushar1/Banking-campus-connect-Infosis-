import pymysql
class transPrint:
    def printi(self,cus):
        conn2=pymysql.connect("localhost","root","","bankM5",autocommit=True)
        cur2=conn2.cursor()
        print("enter the start date in yyyy--mm--dd")
        start_date=raw_input()
        print("enter the end date in yyyy--mm--dd")
        end_date=raw_input()
        print("enter which account statement do you need :")
        acc=raw_input()
        acc=str(acc)
        sq3="SELECT acc_type from account_type where cust_id= "+cus+" and acc_type='"+acc+"'"
        t=cur2.execute(sq3)
        
        if(t==1):
             sq1="SELECT * FROM transact where Date between '"+start_date+"' AND '"+end_date+"' and cust_id= "+cus+" and acc_type= '"+acc+"'"
             #print sq1
             cur2.execute(sq1)
             r=cur2.rowcount
             #print r
             result = cur2.fetchall()
             
             
             print"**************************************************"
             print"|Date      |Transaction Type| Amount |balance  | "
             print"**************************************************"
             for row in result:
                 s1=str(row[3])
                 s2=str(row[2])
                 if(row[4]==0):
                     s=str(row[5])
                     print("|"+s2+"|debit           |"+s+"  |"+s1+"|")
                 else:
                      s=str(row[4])
                      print("|"+s2+"|credit          |"+s+"  |"+s1+"|")
             print("")
             print"**************************************************"
