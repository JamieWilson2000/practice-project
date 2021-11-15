from django.shortcuts import render

# Create your views here.


def pageone(request):
    return render(request, 'home.html')
