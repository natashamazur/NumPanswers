from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('<int:a_id>/', views.article, name='article'),
    path('<int:a_id>/comment/', views.comment, name='comment'),

]
