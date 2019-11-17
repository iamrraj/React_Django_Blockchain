from django.urls import path
from . import views

urlpatterns = [
    path('invoice/', views.IInvoice.as_view()),
    path('invoice/<int:pk>/', views.Dinvoice.as_view()),
]
