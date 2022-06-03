import re
from django.shortcuts import render,redirect
from .models import BlogPost
from django.contrib.auth.models import User
from django.contrib.auth import login ,logout,authenticate
from django.contrib import messages
# Create your views here.

# login and logout views
def userLogin(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user =authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            return redirect('/')
        else:
            messages.error(request,"Username And password Not matching!!!")
            return render(request,'login.html')
    else:
        return render(request,'login.html')

def userRegister(request):
    if request.method == "POST":
        username=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('pass1')
        pass2=request.POST.get('pass2')
        if pass1!=pass2:   
            messages.error(request,"password not matching!!")
            return redirect('/register')
        else:
            newuser=User.objects.create_user(username,email,pass1)
            newuser.save()
            messages.success(request,"Account Created!!! Please Login To Explore")
            return redirect('/')
    return render(request,'register.html')

def usesrLogout(request):
    logout(request)
    return redirect('/')











def index(request):
    blogs=BlogPost.objects.all()
    posts={
        'posts':blogs
    }
    return render(request ,'index.html',posts)

def addPost(request):
    if request.method=="POST":
        title=request.POST.get('title')
        content=request.POST.get('content')
        img=request.FILES.get('img')
        sample=BlogPost(title=title,content=content,img=img,author=request.user)
        sample.save()
    return render(request,'addPost.html')


def viewPost(request,id):
    
    post=BlogPost.objects.get(id=int(id))
    post={
        'post':post
    }
    return render(request,'viewPost.html',post)
    
def viewProfile(request):
    
    posts=BlogPost.objects.filter(author=request.user.id)
    return render(request,'profile.html',{'posts':posts})