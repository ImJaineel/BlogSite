from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# noinspection PyUnresolvedReferences
from blog.models import Post


def home(request):
    # load all the posts from db(10)
    posts = Post.objects.all()[:11]
    # print(posts)
    data = {
        'posts': posts,
    }
    # return HttpResponse('Hello World')
    return render(request, 'home.html', data)