from django.shortcuts import render

# Create your views here.
import cx_Oracle


def grandvitara(request):
    # V15 = []
    if request.method=="GET":
        variant = request.GET.get('variant', None)
        if variant:
            connStr = 'project/project@localhost:1521/xe'
            conn = cx_Oracle.connect(connStr)
            cur = conn.cursor()
            d=request.POST
            sq5 = "SELECT DISTINCT VARIANTNAME  FROM  VARIANTS WHERE MODELNAME='{}'".format(variant)
            print(sq5)
            cur.execute(sq5)  
            V15=cur.fetchall()
            a=tuple(V15)
        context = {'model': V15, 'variant': variant}
        return (render(request, 'varients.html', context))

