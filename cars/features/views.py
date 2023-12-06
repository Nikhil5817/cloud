from django.shortcuts import render
import cx_Oracle
# Create your views here.
# def features(request):
#     if request.method=="GET":
#         lenght = request.GET.get('lenght', None)
#         if lenght:
#             connStr = 'project/project@localhost:1521/xe'
#             conn = cx_Oracle.connect(connStr)
#             cur = conn.cursor()
#             d=request.POST
#             sq5 = "SELECT * FROM  FEATURES WHERE VARIANTNAME= '{}'".format(lenght)
#             print(sq5)
#             cur.execute(sq5)  
#             V17=cur.fetchall()
#             a=tuple(V17)
#         context = {'model': V17}
#         return (render(request, 'features.html', context))  

def features(request):
    V17 = []  # define and initialize V17
    if request.method=="GET":
        features = request.GET.get('features', None)
        print(features)
        if features:
            connStr = 'project/project@localhost:1521/xe'
            conn = cx_Oracle.connect(connStr)
            cur = conn.cursor()
            d=request.POST
            sq5 = "SELECT * FROM  FEATURES WHERE VARIANTNAME= '{}'".format(features)
            print(sq5)
            cur.execute(sq5)  
            V17=cur.fetchall()  # assign value to V17
            a=tuple(V17)
            print(a)
            sq6 = "SELECT DISTINCT VARIANTNAME, MODELNAME, TRANSMISSION,FUELTYPE FROM VARIANTS WHERE VARIANTNAME =  '{}'".format(features)
            print(sq6)
            cur.execute(sq6)  
            V18=cur.fetchall()  # assign value to V17
            a1=tuple(V18)
            print(a1)
            sq7 = "SELECT DISTINCT M.BodyType, M.Price, M.Waitperiod, M.Rating FROM MODELS M JOIN VARIANTS V ON M.ModelName = V.ModelName WHERE V.VariantName = '{}'".format(features)
            print(sq7)
            cur.execute(sq7)  
            V19=cur.fetchall()  # assign value to V17
            a2=tuple(V19)
            print(a1)
        context = {'model1': V17, 'model2': V18,'model3' : V19, 'features': features}
        return (render(request, 'features.html', context)) 

