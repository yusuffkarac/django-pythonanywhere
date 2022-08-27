from django.shortcuts import render
from django.http.response import HttpResponse
from list.models import Product
from django.shortcuts import redirect

# Create your views here.

def index(request):
    context={
        'list': Product.objects.filter(is_bought=False),
    }

    return render(request, 'list/index.html',context)
    

def bought(request):
    context={
        'list': Product.objects.filter(is_bought=True),
    }

    return render(request, 'list/bought.html',context)
    

def add_product(request):
    context={
        'list': Product.objects.all(),
    }

    name = request.GET.get('prname')
    is_bought = request.GET.get('is_bought',"False")
    new_pr = Product(name=name, is_bought=is_bought)
    new_pr.save()
    return redirect("/")

def delete_item(request,id):
    Product.objects.filter(id=id).delete()
    return redirect("/")
def delete_bought_item(request,id):
    Product.objects.filter(id=id).delete()
    return redirect("/bought")

def bought_item(request,id):
    Product.objects.filter(id=id).update(is_bought=True)
    return redirect("/")