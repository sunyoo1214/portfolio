from django.contrib import admin
from django.urls import path, include

from drama import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('drama/', include('drama.urls')),
    path('common/', include('common.urls')),
    path('', views.index, name='index'),
]