

import mysql.connector
from django.shortcuts import render

def features(request):
    V17 = []  # define and initialize V17
    V18 = []  # define and initialize V18
    V19 = []  # define and initialize V19
    features = request.GET.get('features', None)
    print(features)
    if features:
            conn = mysql.connector.connect(
                host='carsdata.cufmhgrmxcfa.ap-south-1.rds.amazonaws.com',
                user='admin',
                password='admin5817',
                database='CARS'
            )
            cursor = conn.cursor(dictionary=True)
            
            sq5 = "SELECT * FROM FEATURES WHERE VARIANTNAME = %s"
            # print(sq5)
            cursor.execute(sq5, (features,))  
            V17 = cursor.fetchall()  # assign value to V17
            print(V17)
            
            sq6 = "SELECT DISTINCT VARIANTNAME, MODELNAME, TRANSMISSION, FUELTYPE FROM VARIANTS WHERE VARIANTNAME = %s"
            # print(sq6)
            cursor.execute(sq6, (features,))
            V18 = cursor.fetchall()  # assign value to V18
            print(V18)

            sq7 = "SELECT DISTINCT M.BodyType, M.Price, M.Waitperiod, M.Rating FROM MODELS M JOIN VARIANTS V ON M.ModelName = V.ModelName WHERE V.VariantName = %s"
            # print(sq7)
            cursor.execute(sq7, (features,))
            V19 = cursor.fetchall()  # assign value to V19
            print(V19)

    context = {'model1': V17, 'model2': V18, 'model3': V19, 'features': features}
    # print(context)
    return render(request, 'features.html', context)




