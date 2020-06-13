from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect, HttpResponse
from app1 import forms
from app1.forms import UserForm
from app1.models import Login_table
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
import os
from django.urls import reverse


def index(request):
    return render(request,'app1/index.html')

def user_login(request):
    form = forms.UserForm()
    if request.method == "POST":
        form = forms.UserForm(request.POST)

        if form.is_valid():
            user = form.data['user']
            password = form.data['password']
            try:
                if (Login_table.objects.get(user=user) and Login_table.objects.get(password=password)):
                    request.session['user'] = form.data['user']
                    request.session['password'] = form.data['password']
                    return redirect('AfterLogin')
                    #return HttpResponseRedirect(reverse('SelectSubmissionType'))
                else:
                    return HttpResponse("Invalid Credentials!")
            except:
                return HttpResponse('<script>alert("Invalid Credentials! Please enter correct login credentials!"); window.location.href="http://10.20.4.65:8000/josusy_app/user_login/";</script>')
        else:
            return render(request,'app1/Login.html',{'form3':form})
    else:
        return render(request,'app1/Login.html',{'form3':form})

def user_registration(request):
    form = forms.UserForm()
    if request.method == "POST":
        form = forms.UserForm(request.POST)

        if form.is_valid():
            un = form.data['user']

            password = form.data['password']
            if bool(Login_table.objects.filter(user=un).exists()):
                #Check for any existing user
                return HttpResponse('<script>alert("User with such credentials already exist! \n Please enter another username! "); window.location.href="http://10.20.4.65:8000/login/";</script>')
            else:
                l1 = Login_table(user=un,password=password)
                l1.save()
                return HttpResponse('<script>alert("User created succesfully!"); window.location.href="http://127.0.0.1:8000/login";</script>')
        else:
            return render(request, 'app1/registration.html',{'form2':form})
    else:
        return render(request, 'app1/registration.html',{'form2':form})

def login_success(request):
    username = request.session['user']
    if bool(username):
        return render(request,'app1/after_login.html')
    else:
        return HttpResponse('<script>alert("Please login for submitting jobsssss!"); window.location.href="http://127.0.0.1:8000/login";</script>')
def mask_detect(request):
    os.system("python mask_detect.py")
    return render(request,'app1/after_mask.html')

#@login_required
def logout(request):

    #username = request.session['user']
    #logoutTime = datetime.datetime.now()
    #Update time in database
    #Login_table.objects.filter(user=username)
    del request.session['user']
    del request.session['password']
    return HttpResponseRedirect(reverse('index'))
