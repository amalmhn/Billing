from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(ItemModel)
admin.site.register(PurchaseModel)
admin.site.register(Order)
admin.site.register(OrderLines)