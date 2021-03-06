"""tryDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import url

from django.views.generic import TemplateView

from restuarants.views import HomeView

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('',home),
    # path('about/',about),
    # path('contact/<int:id>',ContactView.as_view())

    path('',HomeView.as_view()),
    # path('about/',AboutView.as_view()), # AND delete AboutView in views.py
    # path('contact/',ContactView.as_view() # AND delete ContactView in views.py

    path("about/",TemplateView.as_view(template_name='about.html')),
    path("contact/",TemplateView.as_view(template_name='contact.html'))

]
