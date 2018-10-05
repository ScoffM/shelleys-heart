from django.shortcuts import render
from django.shortcuts import get_object_or_404

from .models import Menu


def all_dishes(request):
    dishes = Menu.objects
    return render(request, 'menu/all_dishes.html', {'dishes': dishes})


def detail(request, dish_id):
    detail_dish = get_object_or_404(Menu, pk=dish_id)
    return render(request, 'menu/details.html', {'spell': detail_dish})
