"""cars URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from logincars.views import *
from signup.views import *
from suzuki.views import *
from varients.views import *
from features.views import *
from comparisions.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('logincars', logincars),
    path('signup/',signup),
    path('suzuki/',suzuki),
    path('hyundai/',hyundai),
    path('mahindra/',mahindra),
    path('tata/',tata),
    path('kia/',kia),
    path('toyota/',toyota),
    path('mg/',mg),       
    path('honda/',honda),
    path('skoda/',skoda),
    path('volkswagen/',volkswagen),
    path('benz/',benz),
    path('jeep/',jeep),
    path('bmw/',bmw),
    path('audi/',audi),
    path('landrover/',landrover),
    path('grandvitara/',grandvitara, name='grandvitara'),
    path('features/',features, name='features'),
    path('my_view/',my_view)

    
]
