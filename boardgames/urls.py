from django.urls import path

from . import views

urlpatterns = [
    path('', views.all_games, name='games'),
    path('<str:game_id>/', views.detail, name='game_detail'),
]
