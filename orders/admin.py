from django.contrib import admin
from . models import *

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display=('product_id','product_name','price')
admin.site.register(Product,ProductAdmin)

class OrderAdmin(admin.ModelAdmin):
    list_display=('order_id','customer_id','product','quantity','price','status','order_date')
admin.site.register(Order,OrderAdmin)

class OrderHistoryAdmin(admin.ModelAdmin):
    list_display=('order','action','timestamp')
admin.site.register(OrderHistory,OrderHistoryAdmin)

