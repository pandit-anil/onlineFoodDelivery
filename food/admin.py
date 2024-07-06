from django.contrib import admin
from . models import Restaurant,SystemSetting,MenuItem,DeliveryAddress,Order,OrderItem,Payment

admin.site.register(Restaurant)
admin.site.register(SystemSetting)

@admin.register(MenuItem)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('name','restaurant','price','available')

admin.site.register(DeliveryAddress)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Payment)
