from django.shortcuts import render
# Create your views here.
#Aldığı isteklere uygun fonk.


def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request,'about.html' )

def contact(request):
    return render(request,'contact.html' )

def post(request):
    return render(request,'post.html' )