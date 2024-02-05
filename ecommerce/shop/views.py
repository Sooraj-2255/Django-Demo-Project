from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
from shop.models import Category, Product

from django.contrib.auth.models import User

from django.contrib.auth.models import AbstractUser
from django.contrib.auth import authenticate, login ,logout
from django.contrib.auth.decorators import login_required


def allcategories(request):
    c=Category.objects.all()
    return render(request,'category.html',{'c':c})

def productdetails(request,p):
    c=Category.objects.get(name=p)
    p=Product.objects.filter(category=c)
    return render(request, 'product.html', {'c': c,'p':p})


def details(request,p):
    p=Product.objects.get(name=p)
    return render(request, 'details.html', {'p': p})

def register(request):
    if request.method == "POST":  # works only after form submission
        u = request.POST['u']
        p = request.POST['p']
        cp = request.POST['cp']
        f = request.POST['f']
        l = request.POST['l']
        e = request.POST['e']

        if(p == cp):
            u = User.objects.create_user(username=u, password=p, first_name=f, last_name=l, email=e)
            u.save()
            return redirect('shop:category')
        else:
            return HttpResponse("Passwords are not the same")

    return render(request, 'register.html')


def userlogin(request):
    if request.method == "POST":  # works only after form submission
        u = request.POST['u']
        p = request.POST['p']
        user = authenticate(username=u, password=p)  # Use variables u and p here
        if user:
            login(request, user)
            return redirect('shop:category')
        else:
            return HttpResponse("Invalid Credentials")

    return render(request, 'login.html')



def userlogout(request):
    logout(request)
    return redirect('shop:userlogin')