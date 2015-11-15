from django.shortcuts import render
from BlogRater.models import Category

def index(request):
    # return HttpResponse("Hey There!")
    context_dict = {'boldmessage': "Please search for a blog, if the blog is not in our database, please add one. Then select the blog to view its lastest posts. Click on one of the posts to rate the author of that post.",
                    'search': request.GET['url']
                    }
    return render(request, 'BlogRater/index.html', context_dict)

