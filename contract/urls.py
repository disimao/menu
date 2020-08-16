from django.urls import path
from contract import views


urlpatterns = [

    path('client/<int:pk>/', views.client_detail, name='client-detail'),
    path('client/', views.client_list, name='client-list'),

    path('request/<int:pk>/', views.request_detail, name='request-detail'),
    path('request/', views.request_list, name='request-list'),

    path('clientes/<int:pk>/', views.client_detail, name='cliente-detail'),
    path('clientes/', views.client_list, name='cliente-list'),

    path('pedidos/<int:pk>/', views.request_detail, name='pedidos-detail'),
    path('pedidos/', views.request_list, name='pedidos-list'),


]
