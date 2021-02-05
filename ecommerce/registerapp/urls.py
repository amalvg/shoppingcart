from django.urls import path

from registerapp import views

app_name='registerapp'

urlpatterns = [
    path('login',views.login, name='login'),
    path('register',views.register, name='register'),
    path('logout',views.logout, name='logout'),
]