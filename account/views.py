from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
import random as r




# Create your views here.


def login(request):
    if request.method == "POST":
        email=request.POST['t1']
        password=request.POST['t2']

        if User.objects.filter(email=email).exists():

            return render(request, 'account/welcome.html')
        else:
            msg="user not exist"
            return render(request, 'account/msg.html', {"msg": msg})

    else:
        return render(request,'account/login.html')


def register(request):
    if request.method == "POST":
        username=request.POST['s1']
        email=request.POST['s2']
        password=request.POST['s3']
        #otp=request.POST['s4']
        n=5
        min=pow(10,n-1)
        max=pow(10,n)-1
        b=r.randint(min,max)
        b=str(b)
        print(b)
        user=authenticate(request,username=username,password=password)
        if User.objects.filter(email=email).exists():
            msg="Email-Id Exist"
            return render(request, 'account/msg.html', {"msg": msg})
        elif User.objects.filter(username=username).exists():
            msg="Username Exist"
            return render(request, 'account/msg.html', {"msg": msg})
        elif len(password) < 8:
            msg="Password is too short"
            return render(request, 'account/msg.html',{"msg":msg})
        else:

            #if not request.user.email.endswith('@jmit.ac.in'):
             #   print('4')
            #else:
             #   print('5')
            email_body="hi "+username+\
                       "\" To verify your email-id, use this security " \
                                     "code:"+b+\
                       "If you didn't requested for this code you can safely ignore this email ." \
                       "Someone else might have typed this email by mistake." \
                       "Thankyou "

            send_mail(
                'Account verification' ,
                email_body,
                'from@example.com',
                [email],
                fail_silently=False,
            )
            #if otp==b:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            return render(request, 'account/login.html')

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
