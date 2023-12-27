from django.shortcuts import render
import mysql.connector

username = ''
passwordd = ''

def logincars(request):
    global username, passwordd
    if request.method == "POST":
        conn = mysql.connector.connect(
            host='carsdata.cufmhgrmxcfa.ap-south-1.rds.amazonaws.com',
            user='admin',
            password='admin5817',
            database='CARS'
        )
        cur = conn.cursor(dictionary=True)

        d = request.POST
        for key, value in d.items():
            if key == "email":
                username = value
            if key == "pass":
                passwordd = value

        sq1 = "SELECT * FROM CUSTOMER WHERE Customer_Email = %s AND password = %s"
        print(sq1)
        cur.execute(sq1, (username, passwordd))
        result = cur.fetchall()

        if not result:
            print('fail')
            return render(request, 'fail.html')
        else:
            return render(request, "indexlogout.html")

    return render(request, 'index.html')
