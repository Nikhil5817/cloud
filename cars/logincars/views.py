from django.shortcuts import render

import cx_Oracle

username=''
passwordd=''
# Create your views here.
def logincars(request):
    global email,passwordd
    if request.method=="POST":
        connStr = 'project/project@localhost:1521/xe'

        #connStr = cx_Oracle.connect(user='project', passw  ord='project', dsn='localhost:1521/xe')
        conn = cx_Oracle.connect(connStr)
        cur = conn.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="email":
                username=value
            if key=="pass":
                passwordd=value

        sq1 = "SELECT * FROM CUSTOMER WHERE Customer_Email='{}'AND password='{}'".format(username,passwordd)
        print(sq1)
        cur.execute(sq1)
        a=tuple(cur.fetchall())
       
        if a==():
            print('fail')
            return render(request,'fail.html')
           
        else:
            return render(request,"indexlogout.html")
    return render(request,'index.html')