from django.urls import path
from . import views
app_name = 'purchases'

urlpatterns = [
    path('start/', views.purchase_start_view, name="start"),
    path('success/', views.purchase_success_view, name='success'),
    path('stopped/', views.purchase_stopped_view, name='stopped'),
    path('orders/', views.purchase_order_view, name='orders'),
    path('kakaopay_start/', views.kakaopay_start_view, name='kakaopay_start'),
    path('kakaopay_success/', views.kakaopay_success_view, name='kakaopay_success'),
    path('kakaopay_stop/', views.kakaopay_stop_view, name='kakaopay_stop'),
]
