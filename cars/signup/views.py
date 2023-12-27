from django.shortcuts import render
import mysql.connector

# Create your views here.
firstname = ''
lastname = ''
house_No = ''
city = ''
country = ''
DOB = ''
gender = ''
email = ''
pass_word = ''

def signup(request):
    global firstname, lastname, house_No, city, country, DOB, email, pass_word
    if request.method == "POST":
        conn_details = {
    'host': 'carsdata.cufmhgrmxcfa.ap-south-1.rds.amazonaws.com',
    'user': 'admin',
    'password': 'admin5817',
    'database': 'CARS'
}
        conn = mysql.connector.connect(
            host=conn_details['host'],
            user=conn_details['user'],
            password=conn_details['password'],
            database=conn_details['database']
        )
        cur = conn.cursor()
        d = request.POST
        for key, value in d.items():
            if key == "firstname":
                firstname = value
            if key == "lastname":
                lastname = value
            if key == "houseno":
                house_No = value
            if key == "city":
                city = value
            if key == "country":
                country = value
            if key == "dob":
                DOB = value
            if key == "gender":
                gender = value
            if key == "email":
                email = value
            if key == "pass":
                pass_word = value

        sqltxt = "INSERT INTO CUSTOMER VALUES('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(
            firstname, lastname, house_No, city, country, DOB, gender, email, pass_word)
        cur.execute(sqltxt)
        conn.commit()
        return render(request, 'index.html')
    return render(request, 'signup.html')
