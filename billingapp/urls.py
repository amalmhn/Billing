"""BillingProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from .views import *
urlpatterns = [
    path('item/', ItemCreate.as_view(), name='item'),
    path('purchase/',PurchaseCreate.as_view(), name='purchase'),
    path('view/<int:pk>',PurchaseView.as_view(), name='view'),
    path('edit/<int:pk>',PurchaseEdit.as_view(), name='edit'),
    path('delete/<int:pk>',PurchaseDelete.as_view(), name='delete'),
    path('order',OrderCreate.as_view(), name='order'),
    path('orderline/<str:billnumber>',OrderLinesView.as_view(), name='orderline'),
    path('generate/<str:billnumber>',BillGenerate.as_view(), name='generate')
]
