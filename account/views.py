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
       # b="@jmit.ac.in"
        #for(i=0,i<=11,i++):
         #   if email[-1:-11]!=b(i):
          #      print("mail not valid")
           #     return render(request, 'account/msg.html')

       # else:
        if User.objects.filter(email=email).exists():
            print("emailid is taken by some one else")
            return render(request, 'account/msg.html')
        elif User.objects.filter(username=username).exists():
            print("username not valid")
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

def tutorial(request):
    return render(request,'account/tut_vedio.html')
