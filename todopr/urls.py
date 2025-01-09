from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import render
from tasks.views import register

def home(request):
    return render(request, 'home.html')


urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('tasks/', include('tasks.urls')),
    path('accounts/register/', register, name='register'),
    path('accounts/', include('django.contrib.auth.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
