import pymysql
class address:
    def add_change(self,emp_id):
        conn2=pymysql.connect("localhost","root","","bankM5",autocommit=True)
        cur2=conn2.cursor()
        var=1
        while var==1:
          print("enter your new address")
          ad1=raw_input()
          if(ad1 ==""):
              var=1
          else:
              var=2
        var=1
        while var==1:
          print("enter your new state")
          st1=raw_input()
          if(st1 ==""):
              var=1
          else:
              var=2
        var=1
        while var==1:
          print("enter your new  city")
          ci1=raw_input()
          if(ci1 ==""):
              var=1
          else:
              var=2
        var=1
        while var==1:
          print("enter your new pincode")
          pin=raw_input()
          if(pin ==""):
              var=1
          elif(pin.isdigit()):
              var=2
          else:
              var=1
        sqlA="UPDATE cust_info SET Address = '"+ad1+"' WHERE cust_id= "+emp_id
        cur2.execute(sqlA)
        sqlA="UPDATE cust_info SET State = '"+st1+"' WHERE cust_id= "+emp_id
        cur2.execute(sqlA)
        sqlA="UPDATE cust_info SET Pincode = '"+pin+"' WHERE cust_id= "+emp_id
        cur2.execute(sqlA)
        sqlA="UPDATE cust_info SET City = '"+ci1+"' WHERE cust_id= "+emp_id
        cur2.execute(sqlA)
        print"address changed"
        
