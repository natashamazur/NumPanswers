from django.contrib import admin

# Register your models here.

from .models import User, Article

admin.site.register(User)