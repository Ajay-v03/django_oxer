"""
URL configuration for oxer project.

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
from oxer import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index.html', views.home,name='index.html'),
    path('about.html', views.aboutus,name='about.html'),
    path('blog.html', views.blog,name='blog.html'),
    path('class.html', views.class_type,name='class.html'),
    path('form.html', views.form),
    path('thanks.html', views.thanks,name="thanks.html"),
    path('calculator.html', views.calculator,name="calculator.html"),
]
