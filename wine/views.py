from django.shortcuts import render

def wine(request):
    return render(request, 'index.html', {})

def about(request):
    return render(request, 'about.html', {})

def menu(request):
    return render(request, 'menu.html', {})