from django.shortcuts import render,reverse
from django.http import HttpResponse,HttpResponseRedirect
from .models import *

data=[
        {'id': 1, 'name': 'os'},
        {'id': 2, 'name': 'IOT'},
        {'id': 3, 'name': 'React'}
    ]

data1=[
        {'id': 1, 'name': 'Car'},
        {'id': 2, 'name': 'Pike'},
        {'id': 3, 'name': 'Motor'}
    ]

data2=[
        {'id': 1, 'name': 'Car'},
        {'id': 2, 'name': 'Pike'},
        {'id': 3, 'name': 'Motor'}
    ]

# Create your views here.

#^ list Products
def products(request):
    print(Product.objects.all())
    context={'data':Product.objects.all()}    
    #context={'data':data1}
    return render(request,'products.html', context)

#^ Product Details
def productDetails(request,id):
    product=Product.objects.get(id=id)
    context={'productDetails':product}
    return render(request,'productDetails.html',context)

#^ Add Product
def addProduct(request):
    # print(request.method)
    # print(request.POST)#POST
    # print(request.GET)#GET
    if(request.method=='POST'):
        pName=request.POST['name']
        pPrice=request.POST['price']
        pColor=request.POST['color']
        pImg=request.POST['image']
        pCategory=request.POST['category']
        Product.objects.create(name=pName,price=pPrice,color=pColor,image=pImg, category=pCategory)
        return HttpResponseRedirect(reverse('products'))
    return render(request,'addProduct.html')

#^ deleteProduct
def deleteProduct(request,id):
    Product.objects.filter(id=id).delete()
    return HttpResponseRedirect(reverse('products'))

#^ updateProduct
def updateProduct(request,id):
    context={}
    #post===>update save
    if(request.method=='POST'):
        Product.objects.filter(id=id).update(
            name=request.POST['name'],
            price=request.POST['price'],
            color=request.POST['color'],
            image=request.POST['image'],
            category=request.POST['category'],
        )
        return HttpResponseRedirect(reverse('products'))
    #get--->update.html
    product=Product.objects.get(id=id)
    context['product']=product
    return render(request,'updateProduct.html',context)

#~-------------------------------------------- Categories --------------------------------------------------------------------

#^ list categories
def categories(request):
    print(Category.objects.all())
    context={'data':Category.objects.all()}
    return render(request,'categories.html',context)

#^ Add category
def addCategory(request):
    # print(request.method)
    # print(request.POST)#POST
    # print(request.GET)#GET
    if(request.method=='POST'):
        cName=request.POST['cName']
        Category.objects.create(cName=cName)
        return HttpResponseRedirect(reverse('categories'))
    return render(request,'addCategory.html')

#^ delete Category
def deleteCategory(request,id):
    Category.objects.filter(id=id).delete()
    return HttpResponseRedirect(reverse('categories'))

#^ updateProduct
def updateCategory(request,id):
    context={}
    #post===>update save
    if(request.method=='POST'):
        Category.objects.filter(id=id).update(
            cName=request.POST['cName'],            
        )
        return HttpResponseRedirect(reverse('categories'))
    #get--->update.html
    category=Category.objects.get(id=id)
    context['category']=category
    return render(request,'updateCategory.html',context)


def hello(request):
    return render(request,'Home.html')
    
def home(req):
    return render(req,'Home.html')

def alltracks(req):
    context={'data':data}
    return render(req,'Tracks.html',context)

def mytrack(request,id):
    trackinfo=list(filter(lambda t:t['id']==id,data))
    if(trackinfo):
        context={'trackdata':trackinfo[0]}
        return render(request,'TrackDetails.html',context)
    else:
        return HttpResponse(f'<h1> track not found</h1>')

def about(req):
    return render(req,'About.html')
