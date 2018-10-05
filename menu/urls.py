from django.urls import path

from . import views

urlpatterns = [
    path('', views.all_dishes, name='fullmenu'),
    path('<str:dish_id>/', views.detail, name='detail'),
]