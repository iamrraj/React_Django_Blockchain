from django.urls import path
from . import views

urlpatterns = [
    path('customers/', views.CCustomer.as_view()),
    path('customers/<int:pk>/', views.DCustomer.as_view()),
]
