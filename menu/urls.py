from django.urls import path

from . import views

urlpatterns = [
    path('', views.all_dishes, name='menu'),
    path('<str:dish_id>/', views.detail, name='menu_detail'),
]