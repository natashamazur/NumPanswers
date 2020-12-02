from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('<int:a_id>/', views.article, name='article'),
    path('<int:a_id>/comment/', views.comment, name='comment'),
    path('new_article/', views.new_article, name='new_article'),
    path('post_new_article/', views.post_new_article, name='post_new_article'),

]
