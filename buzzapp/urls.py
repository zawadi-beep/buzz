"""
URL configuration for Buzz project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from buzzapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name = 'index'),
    path('inner-page/', views.inner, name = 'inner'),
    path('portfolio/', views.Portfolio, name = 'portfolio'),
    path('register/', views.register, name = 'register'),
    path('login/', views.login, name = 'login'),
    path('details/', views.detail, name = 'detail'),
    path('user-details/', views.user, name = 'user'),
    path('adminhome/', views.adminhome, name = 'adminhome'),
    path('uploadimage/', views.upload_image, name='upload'),
    path('showimage/', views.show_image, name='image'),
    path('imagedelete/<int:id>', views.imagedelete),
]
