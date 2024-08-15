from django.urls import path
from .import views

urlpatterns=[
    path('payment_success', views.payment_success, name='payment_success'),
    path('checkout', views.checkout, name='checkout'),
    path('billing_info', views.billing_info, name='billing_info'),
    path('process_order', views.process_order, name='process_order'),
    path('shipped_dash', views.shipped_dash, name='shipped_dash'),
    path('orders/<int:pk>', views.orders, name='orders'),
    path('Not_shipped_dash', views.Not_shipped_dash, name='Not_shipped_dash'),
]