from django.urls import path
from . import views

urlpatterns = [
    path('', views.booking_list, name='booking_list'),
    path('create/', views.booking_create, name='booking_create'),
    path('<uuid:booking_id>/', views.booking_detail, name='booking_detail'),
    path('<uuid:booking_id>/update/', views.booking_update, name='booking_update'),
    path('<uuid:booking_id>/delete/', views.booking_delete, name='booking_delete'),
]