from django.shortcuts import render
from BlogRater.models import Author

def index(request):
    # return HttpResponse("Hey There!")
    context_dict = {'boldmessage': "Please search for a blog by entering its url and view all posts. Click on one of the posts to view the content of that post. Then click on \"View Rating\" to rate the author of that post.",
                    'search': request.GET['url']
                    }
    return render(request, 'BlogRater/index.html', context_dict)

def get_author(request):
    author_id = request.GET['id']
    list_of_all_authors = Author.objects.order_by('-rating')

    try :
        author = Author.objects.get(id=author_id)
        context_dict = {'author_id': author_id, 'author_name': author.name, 'author_rating': author.rating, 'list_of_all_authors':list_of_all_authors}
    except:
        Author.objects.create(
            id=author_id,
            name=request.GET['name'],
            rating=0
        )
        author = Author.objects.get(id=author_id)
        context_dict = {'author_id': author_id, 'author_name': author.name, 'author_rating': author.rating, 'list_of_all_authors':list_of_all_authors}

    return render(request, 'BlogRater/author_rating.html', context_dict)

def add_rating(request):
    author_id = request.GET['id']
    list_of_all_authors = Author.objects.order_by('-rating')

    add = request.GET['add']
    author = Author.objects.get(id=author_id)
    author.rating += 1
    author.save()
    context_dict = {'author_id': author_id, 'author_name': author.name, 'author_rating': author.rating, 'list_of_all_authors':list_of_all_authors}

    return render(request, 'BlogRater/author_rating.html', context_dict)