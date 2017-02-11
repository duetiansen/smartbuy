from django.shortcuts import render

def index(request):
    return render(request, 'worksite/index.html')

def about(request):
    return render(request, 'worksite/about.html')

def mail(request):
    return render(request, 'worksite/mail.html')

def products(request):
    return render(request, 'worksite/products.html')

def products1(request):
    return render(request, 'worksite/products1.html')

def products2(request):
    return render(request, 'worksite/products2.html')

def codes(request):
    return render(request, 'worksite/codes.html')

def faq(request):
    return render(request, 'worksite/faq.html')

def icons(request):
    return render(request, 'worksite/icons.html')




