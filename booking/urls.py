from django.urls import path

from . import views

urlpatterns = [
    path('', views.booking, name='booking'),
    # path('<str:dish_id>/', views.detail, name='detail'),
]