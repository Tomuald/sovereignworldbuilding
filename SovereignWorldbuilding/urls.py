"""SovereignWorldbuilding URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('worldbuilder/', include('Project.urls')),
    url('worldbuilder/itemlist/', include('ItemList.urls')),
    url('worldbuilder/universe/pantheon/', include('Pantheon.urls')),
    url('worldbuilder/universe/dungeon/', include('Dungeon.urls')),
    url('worldbuilder/campaign/', include('Campaign.urls')),
    url('worldbuilder/universe/', include('World.urls')),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    url(r'^tinymce/', include('tinymce.urls')),
]
