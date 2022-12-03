from django.shortcuts import render,redirect
from .models import Product
# Create your views here.

def product(request):
    if request.method== 'POST':
        name = request.POST['name']
        weight=request.POST['weight']
        price=request.POST['price']
        product = Product(name=name,weigth=weight,price=price)
        product.save();
        return redirect('allproduct')
    else:
        return render(request,'products/product.html')


def allproduct(request):
    products = Product.objects.all()
    return render(request,'products/allproducts.html',{'products':products})