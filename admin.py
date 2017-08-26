from admin_menu import admin_menu
class admin:
    un="admin"
    pass1="123"
    def check(self):
        print("admin enter your username")
        usee=raw_input()
        print("admin enter your password")
        passw=raw_input()
        
        if usee == self.un :
            if passw == self.pass1 :
                print("your credentials are correct")
                s1=admin_menu()
                s1.menu()
            else:
                print("your credentials are false")
        else:
            print("your credentials are false")
