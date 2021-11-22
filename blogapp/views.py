from django.db import models
from django.shortcuts import redirect, render

from . forms import ModelForm

from . models import post

# Create your views here.


def home(request):
    context = post.objects.all().order_by('-id')
    return render(request,'index.html',{'blogs':context})

def dash(request):
    pst=post.objects.all()
    return render(request,'post_index.html',{'posts':pst})

def single(request,id):
    popular= post.objects.all()
    pst1=post.objects.get(id=id)
    return render(request,'single.html',{'post1':pst1,'blg':popular})


def post_create(request):
    if request.method=='POST':
        title=request.POST.get('title')
        author=request.POST.get('author')
        body=request.POST.get('body')
        img=request.FILES['image']
        p=post(title=title,author=author,body=body,img=img)
        p.save()
        return redirect(dash)
    return render(request,'post_create.html')

def update(request,id):
    object=post.objects.get(id=id)
    form=ModelForm(request.POST or None,request.FILES,instance=object)
    if form.is_valid():
        form.save()
        return redirect(dash)
    return render(request,'edit.html',{'form':form,'object':object}) 

def delete(request,id):
    if request.method=='POST':
        object=post.objects.get(id=id)
        object.delete()
        return redirect(dash)
    return render(request,'delete.html')