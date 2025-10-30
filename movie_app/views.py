from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth.models import User



def index(request):
  return render(request,'index.html')

def home(request):
  return render(request,'home.html')

def login(request):
  if request.method=="POST":
    user_name=request.POST['username']
    password=request.POST['password']

    user=auth.authenticate(username=user_name,password=password)
    if user is not None:
      auth.login(request,user)
      return redirect('home')
    else:
      messages.info(request,"Invalid usrename or password ")
      return redirect('login')
    
  return render(request,"login.html")

def logout(request):
  auth.logout(request)
  return redirect('index')

def register(request):
  if request.method=="POST":
    username=request.POST['user_name']
    first_name=request.POST['first_name']
    last_name=request.POST['last_name']
    gmail=request.POST['email']
    password=request.POST['pass_word']
    confirm=request.POST['confirm']

    if confirm==password:
      if User.objects.filter(username=username).exists():
        messages.info(request,"Username already exist!!!")
        return redirect('register')
      elif User.objects.filter(email=gmail).exists():
        messages.info(request,"Email already exsit!!!!")
        return redirect('register')
      else:
        reg=User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=gmail,password=password)
        reg.save()
        return redirect('login')
  return render(request,'register.html')


def movies(request):
  return render(request,'movies.html')

def series(request):
  return render(request,'series.html')