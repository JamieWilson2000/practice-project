from django.shortcuts import render

# Create your views here.
# Request handler for viewing the home page


def home(request):
    return render(request, 'home/index.html')
