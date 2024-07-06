from django.urls import path
from . import views

urlpatterns = [
        path('login',views.Login,name='login'),
        path('register',views.Register,name='register'),
        path('logout',views.Logout, name = 'logout'),
        path('profile',views.Profile, name='Profile'),
        path('updateprofile',views.UpdateProfile, name='updatep'),
        path('contact',views.Contact,name="contact"),
]
