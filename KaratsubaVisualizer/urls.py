from django.urls import path
from . import views

urlpatterns = [
    path('', views.visualize_karatsuba, name='visualize_karatsuba'),  # Named route for Karatsuba visualizer
]
