from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def register(request):
    if request.method=='POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Exists')
                return redirect('registerapp:register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email Exists')
                return redirect('registerapp{register')
            else:
                user=User.objects.create_user(first_name=first_name,last_name=last_name,username=username,password=password1,email=email)
                user.save()
        else:
            messages.info(request,'Password not matched')
            return redirect('registerapp:register')
        return render(request,'login.html')
    else:
        return render(request,'register.html')

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('ecommerceapp:AllProCat')
        else:
            messages.info(request,'Invalid Credentials')
            return redirect('registerapp:login')
    else:
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('ecommerceapp:AllProCat')