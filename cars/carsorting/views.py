# car_management/views.py
from django.shortcuts import render, redirect
import mysql.connector

conn_details = {
    'host': 'carsdata.cufmhgrmxcfa.ap-south-1.rds.amazonaws.com',
    'user': 'admin',
    'password': 'admin5817',
    'database': 'CARS'
}

def cars_filter_and_sort(request):
    if request.method == 'POST':
        body_type = request.POST.get('bodyType', '')
        min_price = request.POST.get('minPrice', '')
        max_price = request.POST.get('maxPrice', '')
        min_mileage = request.POST.get('mileage', '')

        conn = mysql.connector.connect(
            host=conn_details['host'],
            user=conn_details['user'],
            password=conn_details['password'],
            database=conn_details['database']
        )

        cur = conn.cursor(dictionary=True)

        # Constructing a dynamic SQL query based on input
        sql_query = """
            SELECT 
                M.ModelName, 
                M.BrandName, 
                M.BodyType, 
                M.Rating, 
                M.Price, 
                M.Waitperiod, 
                V.VariantName, 
                V.Transmission, 
                V.FuelType, 
                V.Color, 
                F.Length, 
                F.Width, 
                F.Height, 
                F.Engine_cc, 
                F.Mileage, 
                F.Bootspace, 
                F.Seats, 
                F.Airbags, 
                F.Camera, 
                F.HeadLight
            FROM MODELS M
            JOIN VARIANTS V ON M.ModelName = V.ModelName
            JOIN FEATURES F ON M.ModelName = F.ModelName
            WHERE 1=1
        """

        if body_type:
            sql_query += f" AND M.BodyType = '{body_type}'"

        if min_price:
            sql_query += f" AND M.Price >= {float(min_price)}"

        if max_price:
            sql_query += f" AND M.Price <= {float(max_price)}"

        if min_mileage:
            sql_query += f" AND F.Mileage >= {float(min_mileage)}"

        sql_query += " ORDER BY M.Price ASC"  # You can modify the sorting criteria as needed

        cur.execute(sql_query)
        cars = cur.fetchall()

        conn.close()

        return render(request, 'cars_details.html', {'cars': cars, 'body_type': body_type})

    return render(request, 'cars_details.html', {'cars': [], 'body_type': ''})
