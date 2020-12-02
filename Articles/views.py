from django.http import HttpResponseRedirect

from django.shortcuts import render, reverse

from .models import Article
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

import datetime


def index(request):
    a = Article.objects.order_by('-pub_date')

    return render(request, 'articles/list.html', {'articles': a})


def new_article(request):
    return render(request, 'articles/new_article.html')


def post_new_article(request):
    article_title = request.POST['title']
    article_text = request.POST['text']
    article_author = request.user
    article_pub_date = datetime.datetime.now()

    a = Article.objects.create(title=article_title, text=article_text, pub_date=article_pub_date, author=article_author)
    return HttpResponseRedirect(reverse('articles:article', args=(a.id,)))


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
