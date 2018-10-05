from django.urls import path

from . import views

urlpatterns = [
    path('', views.all_events, name='events'),
    # path('<str:dish_id>/', views.detail, name='detail'),
]