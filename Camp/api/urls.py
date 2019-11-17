from django.urls import path
from . import views

urlpatterns = [
    path('campaign/', views.CCamp.as_view()),
    path('campaign/<int:pk>/', views.DDCamp.as_view()),
]
