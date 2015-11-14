from django.shortcuts import render

def index(request):
    # return HttpResponse("Hey There!")
    context_dict = {'boldmessage': "Please search for an author, if the author is not in our database, please add one."
                    }
    return render(request, 'BlogRater/index.html', context_dict)

