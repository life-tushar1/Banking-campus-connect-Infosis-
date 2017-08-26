import pymysql
import sys
from time import gmtime, strftime
class acc_close:
    def account_closure(self,emp_id):
             #query to close account
         conn2=pymysql.connect("localhost","root","","bankM5",autocommit=True)
         cur2=conn2.cursor()
         sql4="UPDATE cust_info SET Block = 'yes' WHERE cust_id= "+emp_id
         cur2.execute(sql4)
         sql5="UPDATE cust_info SET closed = 'yes' WHERE cust_id= "+emp_id
         cur2.execute(sql5)
         showtime = strftime("%Y-%m-%d %H:%M:%S", gmtime())
         sql1="UPDATE cust_info SET Close_date = '"+showtime+"' WHERE cust_id= "+emp_id
         cur2.execute(sql1)
         print "Your account has been closed successfully contact admin to active it"
