from django.shortcuts import render
from BlogRater.models import Author

def index(request):
    # return HttpResponse("Hey There!")
    context_dict = {'boldmessage': "Please search for a blog, if the blog is not in our database, please add one. Then select the blog to view its lastest posts. Click on one of the posts to rate the author of that post.",
                    'search': request.GET['url']
                    }
    return render(request, 'BlogRater/index.html', context_dict)

def get_author(request):
    author_id = request.GET['id']

    try :
        author = Author.objects.get(id=author_id)
        context_dict = {'author_id': author_id, 'author_name': author.name, 'author_rating': author.rating}
    except:
        Author.objects.create(
            id=author_id,
            name=request.GET['name'],
            rating=0
        )
        author = Author.objects.get(id=author_id)
        context_dict = {'author_id': author_id, 'author_name': author.name, 'author_rating': author.rating}

    return render(request, 'BlogRater/author_rating.html', context_dict)

def add_rating(request):
    author_id = request.GET['id']

    add = request.GET['add']
    author = Author.objects.get(id=author_id)
    author.rating += 1
    author.save()
    context_dict = {'author_id': author_id, 'author_name': author.name, 'author_rating': author.rating}

    return render(request, 'BlogRater/author_rating.html', context_dict)