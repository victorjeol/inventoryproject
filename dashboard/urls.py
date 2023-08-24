from django.urls import path
from . import views


urlpatterns = [
    path('dashboard', views.index, name='index'),
    path('', views.welcome, name='welcome'),
    path('staff', views.staff, name='staff'),
    path('staff/detail/<int:pk>', views.staff_detail, name='staff-detail'),
    path('product', views.product, name='product'),
    path('product/delete/<int:pk>', views.product_delete, name='dashboard-product-delete'),
    path('product/update/<int:pk>', views.product_update, name='dashboard-product-update'),
    path('order', views.order, name='order'),
    # path('login', views.login, name='login'),
]