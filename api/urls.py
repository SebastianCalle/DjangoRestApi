from django.urls import path
from api import views

urlpatterns = [
    path('client/', views.ClientView.as_view()),
    path('client/<int:pk>', views.ClientView.as_view()),
    path('product/', views.ProductView.as_view()),
    path('product/<int:pk>', views.ProductView.as_view()),
    path('bill/', views.BillView.as_view()),
    path('bill-by-client/<int:pk>', views.BillByClientIdView.as_view()),
    path('products-by-bill/<int:pk>', views.ProductsByBillView.as_view()),
    path('bills-by-product/<int:pk>', views.BillByProductView.as_view()),
    path('bill-product/', views.BillProductView.as_view()),
    path('bill-product/<int:pk>', views.BillProductView.as_view()),
    path('client-records', views.CSVView.as_view()),
]