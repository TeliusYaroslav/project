from django.shortcuts import render

# Create your views here.

def contactpage(request):
    return render(request, 'contactpage/contactpage.html')