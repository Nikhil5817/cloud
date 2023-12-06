

# Create your views here.
from django.shortcuts import render
import cx_Oracle
# Create your views here.

firstname=''
lastname =''
house_No = ''
city = ''
country = ''
DOB = ''
gender=''
email=''
pass_word =''


def signup(request):
  global firstname,lastname,house_No,city,country,DOB,email,pass_word
  if request.method=="POST":
    connStr = 'project/project@localhost:1521/xe'
    conn = cx_Oracle.connect(connStr)
    cur = conn.cursor()
    d=request.POST
      #m.close()
    for key,value in d.items():
        if key=="firstname":
                firstname=value
        if key=="lastname":
                lastname=value
        if key=="houseno":
                house_No=value
        if key=="city":
                city=value
        if key=="country":
               country=value
        if key=="dob":
                DOB=value
        if key=="gender":
                gender=value
        if key=="email":
                email=value
        if key=="pass":
                pass_word=value
    #sq1 = "SELECT * FROM CUSTOMER WHERE Customer_Email='{}'AND password='{}'".format(username,passwordd)
    sqltxt="insert into CUSTOMER values('{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(firstname,lastname,house_No,city,country,DOB,gender,email,pass_word)
    cur.execute(sqltxt)
    conn.commit()
    #conn.close()
    return render(request,'index.html')
  return render(request,'signup.html')