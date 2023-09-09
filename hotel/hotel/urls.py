"""
URL configuration for hotel project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

from hotel_app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', start_page, name='start_page'),
    path('rooms/', room_list, name='room_list'),
    path('apply_booking/<int:room_id>/', apply_booking, name='apply_booking'),
    path('booking_success/', booking_success, name='booking_success'),
    path('approve_booking/<int:application_id>/', approve_booking, name='approve_booking'),
    path('reject_booking/<int:application_id>/', reject_booking, name='reject_booking'),
    path('room_detail/<int:room_id>/', room_detail, name='room_detail'),
    path('booking_list/', booking_list, name='booking_list'),
]
