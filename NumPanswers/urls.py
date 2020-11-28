from django.contrib import admin
from django.urls import path, include

app_name='main'
urlpatterns = [
    path('', include('Articles.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
]
