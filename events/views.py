from django.shortcuts import render
# Create your views here.


def all_events(request):
    return render(request, "events/details.html")
