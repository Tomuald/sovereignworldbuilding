from django.urls import path

from .views import homepage

urlpatterns = []

urlpatterns += [
    path('home/', homepage, name="homepage"),
]
