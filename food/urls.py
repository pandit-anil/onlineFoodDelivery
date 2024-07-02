from django.urls import path
from . views import Index,Book,Menu,About


urlpatterns = [
    path('',Index.as_view(),name="home"),
    path('about/',About.as_view(), name='about'),
    path('menu/',Menu.as_view(),name='menu'),
    path('book',Book.as_view(),name='book'),

]
