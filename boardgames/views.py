from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User

users = User.objects.all()


from .models import Game


def all_games(request):
    games = Game.objects
    return render(request, 'boardgames/all.html', {'games': games, 'users': users})


def detail(request, game_id):
    game = get_object_or_404(Game, pk=game_id)
    return render(request, 'boardgames/details.html', {'game': game})
