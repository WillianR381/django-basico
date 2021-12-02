from django.shortcuts import redirect, render, get_object_or_404
from .models import  Produto
from django.http import HttpResponse
from django.template import loader

def index(request):
  produtos = Produto.objects.all()
  context = {
    'curso': 'Dev Django Backend',
    'produtos': produtos ,
  }
  return render(request,'index.html',context)

def contact(request):
  return render(request,'contact.html')  

def product(request, pk):
  # prod = Produto.objects.get(id=pk)
  prod = get_object_or_404(Produto, id=pk)
  context = {
    'produto' : prod
  }
  return render(request,'product.html',context)


def error404(request,ex):
  template = loader.get_template('404.html')
  return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=404)


def error500(request):
  template = loader.get_template('500.html')
  return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=500)