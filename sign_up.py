import pymysql
from time import gmtime, strftime

class sign_up:
   
    def signup_info(self):
        var=1
        while var==1:
         print("enter first name:")
         first=raw_input()
         if(first == ""):
             var=1
         else:
             var=2
        var=1
        while var==1:
         print("enter last name:")
         last=raw_input()
         if(last == ""):
             var=1
         else:
             var=2
        var=1
        while var==1:
         print("enter address:")
         address=raw_input()
         if(address == ""):
             var=1
         else:
             var=2
        var=1
        while var==1:
         print("enter state:")
         state=raw_input()
         if(state == ""):
             var=1
         else:
             var=2
         var=1
         while var==1:
          print("enter your new pincode")
          pincode=raw_input()
          if(pincode ==""):
              var=1
          elif(pincode.isdigit()):
              var=2
          else:
              var=1
        var=1
        while var==1:
         print("enter city:")
         city=raw_input()
         if(city == ""):
             var=1
         else:
             var=2
        conn=pymysql.connect("localhost","root","","bankM5",autocommit=True)
        cur=conn.cursor()
       
        showtime = strftime("%Y-%m-%d %H:%M:%S", gmtime())
        sq3="SELECT * FROM cust_info"
        cur.execute(sq3)
        r=cur.rowcount+1
        r=str(r)
        print("ur new account number is:"+str(r) )
        sql="insert into cust_info values('"+first+"','"+last+"','"+r+"','"+address+"','"+state+"','"+pincode+"','"+city+"','0','self','"+showtime+"','null','null','null')"
        
        
        var2=1
        while var2==1:
            entry=0
            print("enter password")
            passw=raw_input()
            if len(passw)>=8:
              if passw.isalnum():
                print ("strength is good")
                entry=1
              else:
                print("only numeric or alphanumeric")
            else:
              print("minimum 8 charcters are required")
            if(entry == 1):
              print("confirm password")
              conpass=raw_input()
              if passw==conpass:
                var2=2
              else:
                print("wrong confirm password try again:")
        sql4="insert into login values('"+r+"','"+passw+"')"
        
        cur.execute(sql)
        cur.execute(sql4)
        
