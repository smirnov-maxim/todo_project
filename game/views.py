from django.shortcuts import render


def game_page(request):
    return render(request, 'game/game_page.html')