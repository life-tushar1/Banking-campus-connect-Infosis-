import pymysql
class open_fd:
    def regist(self,cus):
        conn=pymysql.connect("localhost","root","","bankM5",autocommit=True)
        cur=conn.cursor()
        sq3="SELECT * FROM fd"
        cur.execute(sq3)
        r=cur.rowcount+1

        print("enter the amount of notes to be deposited in fd in multiple of 1000")
        note=raw_input()
        note=int(note)
        note=note*1000
        note=str(note)
        print("enter the month more than 12 for duration")
        dura=raw_input()
        dura=int(dura)
        if(dura<12):
            print "wrong input fill form again"
        else:
            dura=str(dura)
            sql1="insert into fd values('','"+note+"','"+dura+"','"+cus+"')"
            cur.execute(sql1)
            r=str(r)
            print"ur fd account number is:"+r
            
            
        
