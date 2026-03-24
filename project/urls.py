from django.http import HttpResponse
from django.contrib import admin
from django.urls import path, include

def home(request):
    return HttpResponse("API deu certo, vai para /api/v1/")

urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),
    path('api/v1/', include('api.urls')),
    path('api/v2/', include('api.v2.urls')),
]