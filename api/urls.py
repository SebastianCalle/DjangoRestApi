from django.urls import path
from api import views

urlpatterns = [
    path('client/', views.ClientView.as_view()),
    path('client/<int:pk>', views.ClientView.as_view()),
]