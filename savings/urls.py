from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include,path
from django.contrib.auth.views import *
from django.conf.urls import url
from django.conf.urls.static import static
#urls file
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('savingsapp.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
