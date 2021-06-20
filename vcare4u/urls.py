"""vcare4u URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from care import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('password_reset/',auth_views.PasswordResetView.as_view(),name='password_reset'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
    path('adminlogin', views.admlogin,name = 'adminlogin'),
    path('admindashboard', views.admindonor,name = 'admindashboard'),
    path('adminreceivers', views.adminreceiver,name = 'adminreceivers'),
    path('login',LoginView.as_view(), name='login_url'),
    path('logout',LogoutView.as_view(next_page="home"), name='logout'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('donordashboard',views.donordashboard,name='donordashboard'),
    path('govschemes',views.govschemes,name='govschemes'),
    path('upload', views.upload, name='upload'),
    path('howitworks',views.howitworks, name='howitworks'),
    path('howitworksdonor',views.howitworksdonor, name='howitworksdonor'),
    path("",views.index,name="home"),
    path("registerdonor",views.registerdonor,name="registerdonor"),
    path('ngos',views.ngos,name='ngos'),
    path('donorprofile',views.donorprofile,name='donorprofile'),
    path('receiverdetails',views.receiverdetails,name='receiverdetails'),
]+static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
