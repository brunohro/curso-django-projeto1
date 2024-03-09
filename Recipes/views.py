from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'recipes/pages/home.html') # namespace acompanhando na url 

def recipes(request, id):
    return render(request, 'recipes/pages/recipes-view.html') # namespace acompanhando na url 
