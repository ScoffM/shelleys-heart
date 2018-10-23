from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Game


def all_games(request):
    games = Game.objects
    p2 = [game for game in games.all() if game.players == 2]
    p3 = [game for game in games.all() if game.players == 3]
    p4 = [game for game in games.all() if game.players == 4]

    return render(request, 'boardgames/all.html', {'player2': p2, 'player3': p3, 'player4': p4})


def detail(request, game_id):
    game = get_object_or_404(Game, pk=game_id)
    return render(request, 'boardgames/details.html', {'game': game})
