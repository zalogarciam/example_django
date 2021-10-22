from django.shortcuts import render

# Create your views here.

def home(request):
    name = 'hola'
    numbers = [1, 2, 3 , 4, 5]
    return render(request, 'panel/home.html', locals())