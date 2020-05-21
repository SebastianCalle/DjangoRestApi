from django.contrib import admin
from .models import Client, Product, Bill, BillProducts

admin.site.register(Client)
admin.site.register(Product)
admin.site.register(Bill)
admin.site.register(BillProducts)
# Register your models here.
