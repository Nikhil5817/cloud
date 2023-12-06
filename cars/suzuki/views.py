from django.shortcuts import render
import cx_Oracle

def show_models(request, brand):
    if request.method == "GET":
        jeep = request.GET.get('jeep', None)
        if jeep:
            connStr = 'project/project@localhost:1521/xe'
            conn = cx_Oracle.connect(connStr)
            cur = conn.cursor()
            sq = f"SELECT * FROM MODELS WHERE BRANDNAME = '{brand.upper()}'"
            cur.execute(sq)
            models = cur.fetchall()
            return render(request, 'models.html', {'models': models})
    return render(request, 'models.html')

def search_models(request):
    if request.method == "GET":
        query = request.GET.get('query', None)
        if query:
            connStr = 'project/project@localhost:1521/xe'
            conn = cx_Oracle.connect(connStr)
            cur = conn.cursor()
            sq = f"SELECT * FROM MODELS WHERE MODELNAME LIKE '%{query}%'"
            cur.execute(sq)
            models = cur.fetchall()
            return render(request, 'models.html', {'models': models})
    return render(request, 'models.html')


def suzuki(request):
   # if request.method=="POST":
   connStr = 'project/project@localhost:1521/xe'

   #connStr = cx_Oracle.connect(user='project', passw  ord='project', dsn='localhost:1521/xe')
   conn = cx_Oracle.connect(connStr)
   cur = conn.cursor()
   d=request.POST
   sq1 = "SELECT * FROM MODELS WHERE BRANDNAME = 'MARUTI SUZUKI' "
   print(sq1)
   cur.execute(sq1)
   V=cur.fetchall()
   a=tuple(V)
   #print(V[0][1])
   #return render(request,'suzuki_models.html',{'model': V[0][0]})
   return (render(request, 'models.html', {'model': V, }))

def hyundai(request):
   # if request.method=="POST":
   connStr = 'project/project@localhost:1521/xe'

   #connStr = cx_Oracle.connect(user='project', passw  ord='project', dsn='localhost:1521/xe')
   conn = cx_Oracle.connect(connStr)
   cur = conn.cursor()
   d=request.POST
   sq2 = "SELECT * FROM MODELS WHERE BRANDNAME = 'HYUNDAI' "
   print(sq2)
   cur.execute(sq2)
   V1=cur.fetchall()
   a=tuple(V1)
   return (render(request, 'models.html', {'model': V1 }))



def mahindra(request):
   # if request.method=="POST":
   connStr = 'project/project@localhost:1521/xe'

   #connStr = cx_Oracle.connect(user='project', passw  ord='project', dsn='localhost:1521/xe')
   conn = cx_Oracle.connect(connStr)
   cur = conn.cursor()
   d=request.POST
   sq3 = "SELECT * FROM MODELS WHERE BRANDNAME = 'MAHINDRA' "
   print(sq3)
   cur.execute(sq3)  
   V2=cur.fetchall()
   a=tuple(V2)
   return (render(request, 'models.html', {'model': V2 }))


def tata(request):
   # if request.method=="POST":
   connStr = 'project/project@localhost:1521/xe'

   #connStr = cx_Oracle.connect(user='project', passw  ord='project', dsn='localhost:1521/xe')
   conn = cx_Oracle.connect(connStr)
   cur = conn.cursor()
   d=request.POST
   sq4 = "SELECT * FROM MODELS WHERE BRANDNAME = 'TATA' "
   print(sq4)
   cur.execute(sq4)  
   V3=cur.fetchall()
   a=tuple(V3)
   return (render(request, 'models.html', {'model': V3 }))


def kia(request):
   # if request.method=="POST":
   connStr = 'project/project@localhost:1521/xe'

   #connStr = cx_Oracle.connect(user='project', passw  ord='project', dsn='localhost:1521/xe')
   conn = cx_Oracle.connect(connStr)
   cur = conn.cursor()
   d=request.POST
   sq5 = "SELECT * FROM MODELS WHERE BRANDNAME = 'KIA' "
   print(sq5)
   cur.execute(sq5)  
   V4=cur.fetchall()
   a=tuple(V4)
   return (render(request, 'models.html', {'model': V4 }))


def toyota(request):
   # if request.method=="POST":
   connStr = 'project/project@localhost:1521/xe'

   #connStr = cx_Oracle.connect(user='project', passw  ord='project', dsn='localhost:1521/xe')
   conn = cx_Oracle.connect(connStr)
   cur = conn.cursor()
   d=request.POST
   sq5 = "SELECT * FROM MODELS WHERE BRANDNAME = 'TOYOTA' "
   print(sq5)
   cur.execute(sq5)  
   V5=cur.fetchall()
   a=tuple(V5)
   return (render(request, 'models.html', {'model': V5 }))


def mg(request):
   # if request.method=="POST":
   connStr = 'project/project@localhost:1521/xe'

   #connStr = cx_Oracle.connect(user='project', passw  ord='project', dsn='localhost:1521/xe')
   conn = cx_Oracle.connect(connStr)
   cur = conn.cursor()
   d=request.POST
   sq5 = "SELECT * FROM MODELS WHERE BRANDNAME = 'MG' "
   print(sq5)
   cur.execute(sq5)  
   V6=cur.fetchall()
   a=tuple(V6)
   return (render(request, 'models.html', {'model': V6 }))

def honda(request):
   # if request.method=="POST":
   connStr = 'project/project@localhost:1521/xe'

   #connStr = cx_Oracle.connect(user='project', passw  ord='project', dsn='localhost:1521/xe')
   conn = cx_Oracle.connect(connStr)
   cur = conn.cursor()
   d=request.POST
   sq5 = "SELECT * FROM MODELS WHERE BRANDNAME = 'HONDA' "
   print(sq5)
   cur.execute(sq5)  
   V7=cur.fetchall()
   a=tuple(V7)
   return (render(request, 'models.html', {'model': V7 }))

def skoda(request):
   # if request.method=="POST":
   connStr = 'project/project@localhost:1521/xe'

   #connStr = cx_Oracle.connect(user='project', passw  ord='project', dsn='localhost:1521/xe')
   conn = cx_Oracle.connect(connStr)
   cur = conn.cursor()
   d=request.POST
   sq5 = "SELECT * FROM MODELS WHERE BRANDNAME = 'SKODA' "
   print(sq5)
   cur.execute(sq5)  
   V8=cur.fetchall()
   a=tuple(V8)
   return (render(request, 'models.html', {'model': V8 }))

def volkswagen(request):
   # if request.method=="POST":
   connStr = 'project/project@localhost:1521/xe'

   #connStr = cx_Oracle.connect(user='project', passw  ord='project', dsn='localhost:1521/xe')
   conn = cx_Oracle.connect(connStr)
   cur = conn.cursor()
   d=request.POST
   sq5 = "SELECT * FROM MODELS WHERE BRANDNAME = 'VOLKSWAGEN' "
   print(sq5)
   cur.execute(sq5)  
   V9=cur.fetchall()
   a=tuple(V9)
   return (render(request, 'models.html', {'model': V9 }))

def benz(request):
   # if request.method=="POST":
   connStr = 'project/project@localhost:1521/xe'

   #connStr = cx_Oracle.connect(user='project', passw  ord='project', dsn='localhost:1521/xe')
   conn = cx_Oracle.connect(connStr)
   cur = conn.cursor()
   d=request.POST
   sq5 = "SELECT * FROM MODELS WHERE BRANDNAME = 'MERCEDES BENZ' "
   print(sq5)
   cur.execute(sq5)  
   V10=cur.fetchall()
   a=tuple(V10)
   return (render(request, 'models.html', {'model': V10 }))

def jeep(request):
   # if request.method=="POST":
   connStr = 'project/project@localhost:1521/xe'

   #connStr = cx_Oracle.connect(user='project', passw  ord='project', dsn='localhost:1521/xe')
   conn = cx_Oracle.connect(connStr)
   cur = conn.cursor()
   d=request.POST
   sq5 = "SELECT * FROM MODELS WHERE BRANDNAME = 'JEEP' "
   print(sq5)
   cur.execute(sq5)  
   V11=cur.fetchall()
   a=tuple(V11)
   return (render(request, 'models.html', {'model': V11 }))

def bmw(request):
   # if request.method=="POST":
   connStr = 'project/project@localhost:1521/xe'

   #connStr = cx_Oracle.connect(user='project', passw  ord='project', dsn='localhost:1521/xe')
   conn = cx_Oracle.connect(connStr)
   cur = conn.cursor()
   d=request.POST
   sq5 = "SELECT * FROM MODELS WHERE BRANDNAME = 'BMW' "
   print(sq5)
   cur.execute(sq5)  
   V12=cur.fetchall()
   a=tuple(V12)
   return (render(request, 'models.html', {'model': V12 }))

def audi(request):
   # if request.method=="POST":
   connStr = 'project/project@localhost:1521/xe'

   #connStr = cx_Oracle.connect(user='project', passw  ord='project', dsn='localhost:1521/xe')
   conn = cx_Oracle.connect(connStr)
   cur = conn.cursor()
   d=request.POST
   sq5 = "SELECT * FROM MODELS WHERE BRANDNAME = 'AUDI' "
   print(sq5)
   cur.execute(sq5)  
   V13=cur.fetchall()
   a=tuple(V13)
   return (render(request, 'models.html', {'model': V13 }))

def landrover(request):
   # if request.method=="POST":
   connStr = 'project/project@localhost:1521/xe'

   #connStr = cx_Oracle.connect(user='project', passw  ord='project', dsn='localhost:1521/xe')
   conn = cx_Oracle.connect(connStr)
   cur = conn.cursor()
   d=request.POST
   sq5 = "SELECT * FROM MODELS WHERE BRANDNAME = 'LAND ROVER' "
   print(sq5)
   cur.execute(sq5)  
   V14=cur.fetchall()
   a=tuple(V14)
   return (render(request, 'models.html', {'model': V14 }))


