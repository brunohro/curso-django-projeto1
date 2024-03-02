from django.urls import path
from django.http import HttpResponse
from Recipes.views import home

urlpatterns = [
    path('', home),

]
