from django.http import Http404, HttpResponseRedirect

from django.shortcuts import render

from .models import Article


def index(request):
    a = Article.objects.all()
    return render(request, 'articles/list.html', {'articles': a})
