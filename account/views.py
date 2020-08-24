from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth

# Create your views here.
def login(request):
    if request.method == "POST":
        email=request.POST['t1']
        password=request.POST['t2']
        if User.objects.filter(email=email).exists():
            return render(request, 'account/welcome.html')
        else:
           return render(request,'account/msg.html')
    else:
        return render(request,'account/login.html')


def register(request):
# return render(request,'account/register.html')
#def create(request):
    if request.method == "POST":
        username=request.POST['s1']
        email=request.POST['s2']
        password=request.POST['s3']
        if User.objects.filter(email=email).exists():
            return render(request, 'account/msg.html')
        if User.objects.filter(username=username).exists():
            return render(request, 'account/msg.html')
        else:
            user = User.objects.create_user(username=username,email=email, password=password)
            user.save();
            return render(request,'account/welcome.html')
    else:
        return render(request, 'account/register.html')
def home(request):
    return render(request,'account/home.html')

def contact(request):
    return render(request,'account/contact.html')

def about(request):
    return render(request,'account/about.html')
