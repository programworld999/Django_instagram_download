from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

urlpatterns = [
    path('admin', admin.site.urls),
    path('', include('download.urls')),
    url(r"^submit$", include('download.urls')),
    url(r"^download$", include('download.urls')),
    
]
