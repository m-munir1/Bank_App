"""BankApp URL Configuration

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
from bank_management import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path("step_1", views.step_1, name="step_1"),
    path("step_2", views.step_2, name="step_2"),
    path("step_3", views.step_3, name="step_3"),
    path("bank_management", views.bank_management, name='bank_management'),
    path("bank_management/deposit", views.deposit, name='deposit'),
    path("bank_management/withdraw", views.withdraw, name='withdraw'),
    path("bank_management/balance", views.balance, name='balance'),
    path("bank_management/details", views.details, name='details'),
    path("bank_management/delete", views.delete, name='delete'),
    path("bank_management/logout", views._logout, name='delete'),
]
