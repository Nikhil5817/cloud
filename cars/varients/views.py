from django.shortcuts import render
import mysql.connector

def grandvitara(request):
    variant = request.GET.get('variant', None)
    print(variant)
    V15 = []

    if variant:
        conn_details = {
            'host': 'carsdata.cufmhgrmxcfa.ap-south-1.rds.amazonaws.com',
            'user': 'admin',
            'password': 'admin5817',
            'database': 'CARS'
        }

        try:
            conn = mysql.connector.connect(
                host=conn_details['host'],
                user=conn_details['user'],
                password=conn_details['password'],
                database=conn_details['database']
            )

            cur = conn.cursor(dictionary=True)
            sq5 = "SELECT DISTINCT VARIANTNAME FROM VARIANTS WHERE MODELNAME=%s"
            print(sq5)
            cur.execute(sq5, (variant,))
            V15 = cur.fetchall()
            print(V15)

        except mysql.connector.Error as e:
            print(f"Error: {e}")

        finally:
            if cur:
                cur.close()
            if conn:
                conn.close()

    context = {'model': V15, 'variant': variant}
    print(context)
    return render(request, 'variants.html', context)