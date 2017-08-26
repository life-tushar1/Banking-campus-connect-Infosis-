from admin import admin
from sign_in import sign_in
from sign_up import sign_up
        
var =1
while var == 1:
 print "1 Sign up(new customer)"
 print "2 sign in"
 print "3 admin sign"
 print "4 quit"
 s=raw_input()
 if s=='1':
     s1=sign_up()
     s1.signup_info()
 elif s=='2':
     s2=sign_in()
     s2.signin_info()
 elif s=='3':
     a=admin()
     a.check()
 elif s=='4':
     var=2

