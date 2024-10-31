from django.urls import path
from . import views

urlpatterns = [
    path('', views.n_queens_view, name='n_queens'),
]
