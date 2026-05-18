from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('auto/<int:auto_id>/', views.detalle, name='detalle'),
]