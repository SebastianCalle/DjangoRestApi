from django.urls import path
from api import views

urlpatterns = [
    path('client/', views.ClientView.as_view()),
    path('client/<int:pk>', views.ClientView.as_view()),
    path('product/', views.ProductView.as_view()),
    path('product/<int:pk>', views.ProductView.as_view()),
]