from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    # return HttpResponse("Hey There!")
    context_dict = {'boldmessage': "Please first click one of the following RateAuthors App to start using them:"}
    return render(request, 'RateAuthorsMainApp/index.html', context_dict)

