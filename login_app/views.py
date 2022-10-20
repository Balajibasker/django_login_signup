from django.shortcuts import render,redirect
from rest_framework.response import Response
# Create your views here.
from rest_framework.decorators import api_view
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.contrib.auth import authenticate,login

@csrf_exempt
def index(request):
    return render(request,'index.html')

# @csrf_exempt
# def signin(request):
#     pass
# @csrf_exempt
# def register(request):
#     if request.method=="POST":

#         uname =request.POST.get("uname")
#         email=request.POST.get("email")
#         psw=request.POST.get("pass")

#         print(uname,email,psw)
#         #myuser=User.objects.create_user(uname,email,password)
#        # myuser.save()
#         return HttpResponse("signup successfull")
#     return render(request,'register.html')


@csrf_exempt
def signin(request):
    if request.method=="POST":

        uname=request.POST.get("uname")
        pass1=request.POST.get("password")
        #print(uname,pass1)
        myuser=authenticate(username=uname,password=pass1)
        if myuser is not None:
            login(request,myuser)
            messages.success(request,"Login Success")
            return HttpResponse('hai welcome')
        else:
            messages.error(request,"Invalid Crendentails")
            return redirect('/signupN ')
            #return render(request,"register.html")
    return render(request,"index.html")


@csrf_exempt
def signup(request):
    if request.method=="POST":

        uname =request.POST.get("uname")
        email =request.POST.get("email")
        psw1  =request.POST.get("pass1")
        psw2  =request.POST.get("pass2")

        print(uname,email,psw1,psw2)
        if psw1 != psw2:
            #return HttpResponse("password incorrect")
            messages.warning(request,"Password doesn't match")
            return redirect('/signup')
        #myuser=User.objects.create_user(uname,email,psw1,psw2)
        #myuser.save()
        try:
            if User.objects.get(username=uname):
                messages.info(request,"Username is already taken")
                return redirect('/signup')
        except:
            pass
        try:
            if User.objects.get(email=email):
                messages.info(request,"Email is already taken")
                return redirect('/signup')
                
        except:
            pass
        myuser=User.objects.create_user(uname,email,psw1)
        myuser.save()
        messages.info(request,"SignUp Successfull ")
        redirect('/signin')
        #return HttpResponse('registered')
    return render(request,'index.html')

    def signinn():
        pass