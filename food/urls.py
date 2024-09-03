from django.urls import path
from . views import Book,About
from . import views
from . import views


urlpatterns = [
    path('',views.Index,name="home"),
    path('about/',About.as_view(), name='about'),
    path('menu/',views.MenuItems,name='menu'),
    path('details/<int:id>',views.Detail, name="details"),
    path('offer-detail/<int:id>', views.OfferView,name= "offerview"),
    path('add-to-order/<int:order_id>/', views.AddOrder, name='add_to_order'),
    path('order',views.OrderView,name='order'),
    path('remove/<int:order_id>',views.remove_Order,name="remove"),
    path('increse-order/<int:order_id>',views.increase_quantity,name="increaseOrder"),
    path('decrease-order/<int:order_id>',views.decrease_quantity,name="decrease"),
    path('payment',views.proceed_to_payment, name="payment"),
    path('restaurant',views.SelectRestaurant , name="restaurant"),
    path('selecttable/<int:hotel_id>',views.SelectTable,name="selecttable"),
    path('billview',views.BillView,name="billview"),


]
