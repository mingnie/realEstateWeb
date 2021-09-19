
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.urls import path, include

urlpatterns = [
    path('', include('pages.urls')),
    path('admin/', admin.site.urls),
]