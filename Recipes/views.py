from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'recipes/home.html') # namespace acompanhando na url 

def sobre(request):
    return render(request, 'recipes/sobre.html')

