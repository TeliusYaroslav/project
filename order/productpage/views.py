from django.shortcuts import render

# Create your views here.
def productpage(request):
    return render(request, 'productpage/productpage.html')

def productpage2(request):
    return render(request, 'productpage/clothes1.html')

def productpage3(request):
    return render(request, 'productpage/clothes2.html')

def productpage4(request):
    return render(request, 'productpage/shoes.html')

    