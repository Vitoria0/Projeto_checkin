from django.urls import path
from django.contrib import admin
from django.urls.resolvers import URLPattern
from django.conf.urls import url, include

urlpatterns = [
    url(r'^', include('polls.urls')),
    path('admin/', admin.site.urls),

]