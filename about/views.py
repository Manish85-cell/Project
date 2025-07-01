from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request ,"about/index.html")


def intro(request):
    return render(request, 'about/intro.html')

def blog(request):
    return render(request, 'about/blog.html')

def cv(request):
    return render(request, 'about/cv.html')

def contact(request):
    return render(request, 'about/contact.html')