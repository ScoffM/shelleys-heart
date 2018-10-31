from django.urls import path

from . import views

urlpatterns = [
    path('', views.static_menu, name='menu'),
    path('dynamic_menu', views.all_dishes, name='dmenu'),
    path('<str:dish_id>/', views.detail, name='menu_detail'),
]