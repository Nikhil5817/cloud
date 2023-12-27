from django.shortcuts import render
import mysql.connector

conn_details = {
    'host': 'carsdata.cufmhgrmxcfa.ap-south-1.rds.amazonaws.com',
    'user': 'admin',
    'password': 'admin5817',
    'database': 'CARS'
}




def suzuki(request):
    conn = mysql.connector.connect(
        host=conn_details['host'],
        user=conn_details['user'],
        password=conn_details['password'],
        database=conn_details['database']
    )

    cur = conn.cursor(dictionary=True)
    sq1 = "SELECT * FROM MODELS WHERE BRANDNAME = 'MARUTI SUZUKI' "
    print(sq1)
    cur.execute(sq1)
    V = cur.fetchall()
    print(V[0])
    return render(request, 'models.html', {'model': V})


def hyundai(request):
    conn = mysql.connector.connect(
        host=conn_details['host'],
        user=conn_details['user'],
        password=conn_details['password'],
        database=conn_details['database']
    )

    cur = conn.cursor(dictionary=True)
    sq2 = "SELECT * FROM MODELS WHERE BRANDNAME = 'HYUNDAI' "
    print(sq2)
    cur.execute(sq2)
    V1 = cur.fetchall()
    return render(request, 'models.html', {'model': V1})


def mahindra(request):
    conn = mysql.connector.connect(
        host=conn_details['host'],
        user=conn_details['user'],
        password=conn_details['password'],
        database=conn_details['database']
    )

    cur = conn.cursor(dictionary=True)
    sq3 = "SELECT * FROM MODELS WHERE BRANDNAME = 'MAHINDRA' "
    print(sq3)
    cur.execute(sq3)
    V2 = cur.fetchall()
    return render(request, 'models.html', {'model': V2})


def tata(request):
    conn = mysql.connector.connect(
        host=conn_details['host'],
        user=conn_details['user'],
        password=conn_details['password'],
        database=conn_details['database']
    )

    cur = conn.cursor(dictionary=True)
    sq4 = "SELECT * FROM MODELS WHERE BRANDNAME = 'TATA' "
    print(sq4)
    cur.execute(sq4)
    V3 = cur.fetchall()
    return render(request, 'models.html', {'model': V3})


def kia(request):
    conn = mysql.connector.connect(
        host=conn_details['host'],
        user=conn_details['user'],
        password=conn_details['password'],
        database=conn_details['database']
    )

    cur = conn.cursor(dictionary=True)
    sq5 = "SELECT * FROM MODELS WHERE BRANDNAME = 'KIA' "
    print(sq5)
    cur.execute(sq5)
    V4 = cur.fetchall()
    return render(request, 'models.html', {'model': V4})


def toyota(request):
    conn = mysql.connector.connect(
        host=conn_details['host'],
        user=conn_details['user'],
        password=conn_details['password'],
        database=conn_details['database']
    )

    cur = conn.cursor(dictionary=True)
    sq5 = "SELECT * FROM MODELS WHERE BRANDNAME = 'TOYOTA' "
    print(sq5)
    cur.execute(sq5)
    V5 = cur.fetchall()
    return render(request, 'models.html', {'model': V5})


def mg(request):
    conn = mysql.connector.connect(
        host=conn_details['host'],
        user=conn_details['user'],
        password=conn_details['password'],
        database=conn_details['database']
    )

    cur = conn.cursor(dictionary=True)
    sq5 = "SELECT * FROM MODELS WHERE BRANDNAME = 'MG' "
    print(sq5)
    cur.execute(sq5)
    V6 = cur.fetchall()
    return render(request, 'models.html', {'model': V6})


def honda(request):
    conn = mysql.connector.connect(
        host=conn_details['host'],
        user=conn_details['user'],
        password=conn_details['password'],
        database=conn_details['database']
    )

    cur = conn.cursor(dictionary=True)
    sq5 = "SELECT * FROM MODELS WHERE BRANDNAME = 'HONDA' "
    print(sq5)
    cur.execute(sq5)
    V7 = cur.fetchall()
    return render(request, 'models.html', {'model': V7})


def skoda(request):
    conn = mysql.connector.connect(
        host=conn_details['host'],
        user=conn_details['user'],
        password=conn_details['password'],
        database=conn_details['database']
    )

    cur = conn.cursor(dictionary=True)
    sq5 = "SELECT * FROM MODELS WHERE BRANDNAME = 'SKODA' "
    print(sq5)
    cur.execute(sq5)
    V8 = cur.fetchall()
    return render(request, 'models.html', {'model': V8})


def volkswagen(request):
    conn = mysql.connector.connect(
        host=conn_details['host'],
        user=conn_details['user'],
        password=conn_details['password'],
        database=conn_details['database']
    )

    cur = conn.cursor(dictionary=True)
    sq5 = "SELECT * FROM MODELS WHERE BRANDNAME = 'VOLKSWAGEN' "
    print(sq5)
    cur.execute(sq5)
    V9 = cur.fetchall()
    return render(request, 'models.html', {'model': V9})


def benz(request):
    conn = mysql.connector.connect(
        host=conn_details['host'],
        user=conn_details['user'],
        password=conn_details['password'],
        database=conn_details['database']
    )

    cur = conn.cursor(dictionary=True)
    sq5 = "SELECT * FROM MODELS WHERE BRANDNAME = 'MERCEDES BENZ' "
    print(sq5)
    cur.execute(sq5)
    V10 = cur.fetchall()
    return render(request, 'models.html', {'model': V10})


def jeep(request):
    conn = mysql.connector.connect(
        host=conn_details['host'],
        user=conn_details['user'],
        password=conn_details['password'],
        database=conn_details['database']
    )

    cur = conn.cursor(dictionary=True)
    sq5 = "SELECT * FROM MODELS WHERE BRANDNAME = 'JEEP' "
    print(sq5)
    cur.execute(sq5)
    V11 = cur.fetchall()
    return render(request, 'models.html', {'model': V11})


def bmw(request):
    conn = mysql.connector.connect(
        host=conn_details['host'],
        user=conn_details['user'],
        password=conn_details['password'],
        database=conn_details['database']
    )

    cur = conn.cursor(dictionary=True)
    sq5 = "SELECT * FROM MODELS WHERE BRANDNAME = 'BMW' "
    print(sq5)
    cur.execute(sq5)
    V12 = cur.fetchall()
    return render(request, 'models.html', {'model': V12})


def audi(request):
    conn = mysql.connector.connect(
        host=conn_details['host'],
        user=conn_details['user'],
        password=conn_details['password'],
        database=conn_details['database']
    )

    cur = conn.cursor(dictionary=True)
    sq5 = "SELECT * FROM MODELS WHERE BRANDNAME = 'AUDI' "
    print(sq5)
    cur.execute(sq5)
    V13 = cur.fetchall()
    return render(request, 'models.html', {'model': V13})


def landrover(request):
    conn = mysql.connector.connect(
        host=conn_details['host'],
        user=conn_details['user'],
        password=conn_details['password'],
        database=conn_details['database']
    )

    cur = conn.cursor(dictionary=True)
    sq5 = "SELECT * FROM MODELS WHERE BRANDNAME = 'LAND ROVER' "
    print(sq5)
    cur.execute(sq5)
    V14 = cur.fetchall()
    return render(request, 'models.html', {'model': V14})
