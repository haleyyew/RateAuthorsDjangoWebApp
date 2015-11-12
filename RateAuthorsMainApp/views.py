from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    # return HttpResponse("Hey There!")
    context_dict = {'boldmessage': "Please first click \"Load Data\" to load all tracks on SoundCloud to the table, then click on a track in the table below to play the track."}
    return render(request, 'RateAuthorsMainApp/index.html', context_dict)

