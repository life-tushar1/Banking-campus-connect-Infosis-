from print_close import print_close
from fd_report import fd_report
from fd_cust_via import fd_cust_via
from fd_wrt import fd_wrt
from fd_not import fd_not
from loan_report import loan_report
from loan_cust_via import loan_cust_via
from loan_wrt import loan_wrt
from loan_not import loan_not
from fd_load_not import fd_loan_not
class admin_menu:
    def menu(self):
        var2 = 1
        while (var2 == 1):
                print "1 PRINT CLOSED ACCOUNT HISTORY"
                print "2 FD REPORT OF CUSTOMER"
                print "3 FD REPORT OF CUSTOMER VIA ANOTHER CUSTOMER"
                print "4 FD REPORT W.R.T A PARTICULAR FD AMOUNT"
                print "5 LOAN REPORT OF CUSTOMER"
                print "6 LOAN REPORT OF CUSTOMER VIA ANOTHER CUSTOMER"
                print "7 LOAN REPORT W.R.T LOAN AMOUNT"
                print "8 REPORT OF CUSTOMERS WHO ARE YET TO AVAIL A LOAN"
                print "9 REPORT OF CUSTOMERS WHO ARE YET TO OPEN AN FD ACCOUNT"
                print "10 REPORT OF CUSTOMERS WHO NEITHER HAVE A LOAN NOR A FD ACCOUNT WITH THE BANK"
                print "11 ADMIN LOGOUT"
                c = int(input())
                if(c==1):
                    a=print_close()
                    a.printi()
                elif(c==2):
                    a=fd_report()
                    a.report()
                elif(c==3):
                    a=fd_cust_via()
                    a.via()
                         
                elif(c==4):
                    a=fd_wrt()
                    a.wrt()

                elif(c==5):
                    a=loan_report()
                    
                    a.report()
                elif(c==6):
                    a=loan_cust_via()
                    a.via()
                elif(c==7):
                    a=loan_wrt()
                    a.wrt()
                elif(c==8):
                    a=loan_not()
                    a.loan()
                elif(c==9):
                    a=fd_not()
                    a.fd()
                elif(c==10):
                    a=fd_loan_not()
                    a.noti()
                elif(c==11):
                    var2=2
                elif(c>=12 and c<1):
                    print"wrong input try again"
                    
                