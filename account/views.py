from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth

# Create your views here.
def logbtn(request):
    if request.method == "POST":
        emailid=request.POST['t1']
        password=request.POST['t2']
        if User.objects.filter(emailid=emailid).exists():
            return render(request, 'account/home.html')
        else:
            msg="User Not Found"
            return render(request,'msg.html',{"msg":msg})

def login(request):
    return render(request,'account/login.html')


def register(request):
    return render(request,'account/register.html')
def create(request):
    if request.method == "POST":
        username=request.POST['s1']
        emailid=request.POST['s2']
        password=request.POST['s3']
        if User.objects.filter(emailid=emailid).exists():
            msg="EmailId Taken"
            return render(request, 'msg.html',{{"msg":msg}})
        if User.objects.filter(username=username).exists():
            msg="Username Taken"
            return render(request, 'msg.html',{{"msg":msg}})
        else:
            user = User.objects.create_user(username=username,emailid=emailid, password=password)
            user.save();
            return render(request,'account/home.html')

def home(request):
    return render(request,'account/home.html')

def contact(request):
    return render(request,'account/contact.html')

def about(request):
    return render(request,'account/about.html')
