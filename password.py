class password:
    def checkpass(self):
      passw = str(raw_input("password: "))
      if len(passw)>=8:
       if passw.isalnum():
          print ("strength is good")
       else:
            print("only numeric or alphanumeric")
      else:
            print("minimum 8 charcters are required")
b=password()
b.checkpass()
