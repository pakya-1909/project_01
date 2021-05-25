from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def login_page(request):
    return render(request, 'login_page.html')

def registration_page(request):
    return render(request, 'registration_page.html')

def shop_list(request):
    return render(request, 'shop_list.html')

def product_list(request):
    return render(request, 'product_list.html')