from django.urls import path
from django.http import HttpResponse
from Recipes.views import home, sobre

urlpatterns = [
    path('', home),
    path('sobre/', sobre)
]
