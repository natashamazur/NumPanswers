from django.db import models


class User(models.Model):
    login = models.CharField('Логин', max_length=20)
    name = models.CharField('Псевдоним', max_length=20)


class Article(models.Model):
    title = models.CharField('Название статьи', max_length=200)
    text = models.TextField('Тест статьи')
    pub_date = models.DateTimeField('Дата публикации')
    author = models.ForeignKey(User, on_delete=models.CASCADE)


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField('Текст комментария')



