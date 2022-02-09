from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request, 'pages/home.html')

def about(request):
    return render(request, 'pages/about.html')

def servies(request):
    return render(request, 'pages/servies.html')

def contact(request):
    return render(request, 'pages/contact.html')