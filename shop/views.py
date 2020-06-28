from django.shortcuts import render
from django.http import HttpResponse
from .models import product
from math import ceil
# Create your views here.
def index(request):
	# products=product.objects.all()
	# print(products)
	# n=len(products)
	# nSlides=n//4 + ceil((n/4)-(n//4))
	allProds=[]
	catProds=product.objects.values('category', 'id')
	# print(catProds)
	cats={item['category'] for item in catProds}
	# print(cats)
	for cat in cats:
		prod=product.objects.filter(category=cat)
		n=len(prod)
		nSlides=n//4 + ceil((n/4)-(n//4))
		allProds.append([prod, range(1, nSlides), nSlides ])
	# allProds=[[products, range(1 , nSlides),nSlides],
	# [products, range(1 , nSlides),nSlides]]
	# params={'noOfSlides':nSlides,'range': range(1,nSlides),'product':products}
	params={'allProds':allProds}
	return render(request,'shop/index.html',params)



  

def about(request):
    return render(request,'shop/about.html')

def contact(request):
	return HttpResponse('we are at the contact')

def tracker(request):
	return HttpResponse('we are at the tracker')

def search(request):
	return HttpResponse('we are at the search')

def productView(request):
	return HttpResponse('we are at the product view')

def checkOut(request):
	return HttpResponse('we are at the check out')


