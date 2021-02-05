from django.urls import path
from ecommerceapp import views

app_name='ecommerceapp'

urlpatterns = [
    path('', views.AllProCat, name='AllProCat'),
    path('<slug:c_slug>/', views.AllProCat, name='product_by_category'),
    path('<slug:c_slug>/<slug:p_slug>/', views.procatdetail, name='procatdetail'),
]
