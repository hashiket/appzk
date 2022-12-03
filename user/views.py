from django.shortcuts import render, redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import Post


# Create your views here.

def index(request):
    return render(request,"user/main.html")


def login(request):
    if request.method== 'POST':
        username=request.POST['username']
        password=request.POST['password']
        print(username)
        print(password)
        user=auth.authenticate(request,username=username,password=password)
        if user:
                auth.login(request,user)
                return redirect("/")
        else:
            messages.info(request,"Invalid Credentials")
            return redirect("login")
    else:
        return render(request,"user/login.html")


def logout(request):
    auth.logout(request)
    return redirect('/')


def register(request):
    if request.method == 'POST':
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        username=request.POST.get('username')
        email=request.POST.get('email')
        password1=request.POST.get('password1')
        password2=request.POST.get('password2')
        if password1==password2:
             if User.objects.filter(username=username).exists():
                   messages.info(request,'Username Taken')
                   return redirect('register')
             else:
                  user=User.objects.create_user(first_name=first_name,last_name=last_name,email=email,username=username,password=password1)
                  user.save();

                 

                  print('user created')
                  return redirect('login')
        else:
            messages.info(request,'password not matching...')
            return redirect('register')
        return redirect('/')   
    else:
        return render(request,"user/register.html")



def pomain(request):
    return render(request,"user/pomain.html")

def post(request):
    if request.method == "POST":
        des=request.POST.get('desc')
        spost = Post(user=request.user,text=des)
        spost.save();
        return redirect("allpost") 
    else:
        return render(request,"user/post.html")

def allpost(request):
    posts = Post.objects.all()
    return render(request,"user/allpost.html",{'posts':posts})
