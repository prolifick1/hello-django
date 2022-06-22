"""hello_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
import math

def rectArea(request, height, width):
    response = HttpResponse(f'<h1>{height * width}<h1>')
    response.status_code = 400
    return response;
def rectPerimeter(request, height, width):
    response = HttpResponse(f'<h1>{2*height + 2*width}<h1>')
    response.status_code = 400
    return response;
def circArea(request, radius):
    response = HttpResponse(f'<h2>{round(math.pi*(radius)**2, 2)}</h2>')
    response.status_code = 400
    return response;
def circPerimeter(request, radius):
    response = HttpResponse(f'<h2>{round(math.pi*2*radius, 2)}')
    response.status_code = 400
    return response;

urlpatterns = [
    path('rectangle/area/<int:height>/<int:width>', rectArea), 
    path('rectangle/perimeter/<int:height>/<int:width>', rectPerimeter), 
    path('circle/area/<int:radius>', circArea), 
    path('circle/perimeter/<int:radius>', circPerimeter), 
    path('admin/', admin.site.urls),
]
