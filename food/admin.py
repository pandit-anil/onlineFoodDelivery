from django.contrib import admin
from . models import Restaurant,SyatemSetting,MenuItem,DeliveryAddress,Order,OrderItem,Payment

admin.site.register(Restaurant)
admin.site.register(SyatemSetting)
admin.site.register(MenuItem)
admin.site.register(DeliveryAddress)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Payment)
