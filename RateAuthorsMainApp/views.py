from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    # return HttpResponse("Hey There!")
    context_dict = {'boldmessage': "Please find a blog in our list that you want to rate."}
    return render(request, 'RateAuthorsMainApp/index.html', context_dict)

