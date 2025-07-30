from django.shortcuts import render,redirect
from.models import Product
from.models import Customer
from.models import Sale
from django.forms import ModelForm

class ProductForm(ModelForm):
    class Meta:
        model=Product
        fields='__all__' 

def add_product(request):
    form =ProductForm()
    if request.method =='POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product-list')
    return render(request,'billing/product_form.html',{'form':form})
        
def product_list(request):
    products =Product.objects.all()
    return render(request,'billing/product_list.html',{'products':products})

class CustomerForm(ModelForm):
    class Meta:
        model=Customer
        fields='__all__' 

def add_customer(request):
    form =CustomerForm()
    if request.method =='POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer-list')
    return render(request,'billing/customer_form.html',{'form':form})
        
def customer_list(request):
    customers =Customer.objects.all()
    return render(request,'billing/customer_list.html',{'customers':customers})

class SaleForm(ModelForm):
    class Meta:
        model=Sale
        fields=['customer','product','quantity']
def add_sale(request):
    form =SaleForm()
    if request.method =='POST':
        form = SaleForm(request.POST)
        if form.is_valid():
           instance= form.save()
           print("SALE SAVED:",instance)
           return redirect('sale-list')
        else:
            print("ERRORS:", form.errors)
    else:
        form = SaleForm()
        
    return render(request,'billing/sale_form.html',{'form':form})
        
def sale_list(request):
    sales =Sale.objects.all()
    return render(request,'billing/sale_list.html',{'sales':sales})

def Home_page(request):
    return render(request,'billing/Home_page.html')

