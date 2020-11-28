from django.http import HttpResponseRedirect

from django.shortcuts import render, reverse

from .models import Article
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


def index(request):
    a = Article.objects.order_by('-pub_date')

    return render(request, 'articles/list.html', {'articles': a})


def register(request):
    username = request.POST['username']
    password = request.POST['password']
    user = User.objects.create_user(username, None, password)
    user.save()
    login(request, user)
    return HttpResponseRedirect(reverse('articles:index'))


def article(request, a_id):
    a = Article.objects.get(id=a_id)
    c = a.comment_set.all()
    return render(request, 'articles/article.html', {'article': a, 'comments': c})


def comment(request, a_id):
    a = Article.objects.get(id=a_id)
    comment_text = request.POST['text']
    a.comment_set.create(text=comment_text, article=a, author=request.user)
    return HttpResponseRedirect(reverse('articles:article', args=(a.id,)))
