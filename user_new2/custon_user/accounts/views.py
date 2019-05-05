from django.shortcuts import render,redirect
from .forms import RegisterForm,LoginForm
# Create your views here.
from django.contrib.auth import authenticate,login
def index(request):
    form=RegisterForm(request.POST or None)
    context={'form':form}
    if form.is_valid():
        form.save()
    return render(request,'accounts/register.html',context)
def Login(request):
    form=LoginForm(request.POST)
    context={'form':form}
    if form.is_valid():
        email=form.cleaned_data.get('email')
        username=form.cleaned_data.get('username')
        password=form.cleaned_data.get('password')
        user=authenticate(email=email,password=password,username=username)
        login(request,user)
        return redirect('/admin')
    return render(request,'accounts/login.html',context)