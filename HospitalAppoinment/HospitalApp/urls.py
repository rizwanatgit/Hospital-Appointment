"""HospitalAppoinment URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from .import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path("",views.indexpage),
    path("login", views.loginpage),
    path("signup",views.signuppage),
    path("homepage",views.homepage),
    path("signUP",views.signUP),
    path("AppoinmentAction",views.AppoinmentAction),
    path("logout",views.logout),
    path("adminlog",views.adminlog),
    path("appoinment",views.appoinment),
    path("bookings",views.booking_details),
    path("adminhome",views.adminhome),
    path("logincheck",views.adminLog),
    path("appoinments",views.pending_app),
    path("approve_app/<id>",views.accept_app),
    path("doctors",views.doctors_pg),
    path("adddoctor",views.AddDoctor),
    path("doctortable",views.doctortable),
    path("docdelete/<id>",views.docdelete)

]
