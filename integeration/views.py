
from django.shortcuts import redirect, render,HttpResponse,HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from .models import Coffee
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, UserManager
import razorpay
from django.views.decorators.csrf import csrf_exempt


# home
def home(request):
    return render(request,"integeration/home.html")

def payment(request):
    if request.method=="POST":
        uname=request.POST['name']
        amount=int(request.POST['amount'])*100
        client=razorpay.Client(auth=("rzp_test_ctHeJCHQBtAKoT","BVUsUIwD1SV3Fv7mPG7AtADb"))
        payment=client.order.create({'amount':amount,'currency':'INR','payment_capture':'1'}) 
        coffee=Coffee(name=uname,amount=amount,payment_id=payment['id'])   
        return render(request,"integeration/index.html",{'payment':payment,'uname':uname})     
 
    return render(request,"integeration/index.html")



# signup form 

def sign_up(request,username=None):
    if request.method=="POST":
        username=request.POST['name']
        email=request.POST['email']
        password=request.POST['password']
        confirmPassword=request.POST['confirmPassword']
        

        if(password==confirmPassword):
            if User.objects.filter(username=username).exists():
                messages.warning(request,'UserName is Already Taken')
                return HttpResponseRedirect('/sign/')
            else:
                rg=User.objects.create_user(username=username,email=email,password=password)
                rg.save()
                messages.success(request," SuccessFully Account created !! Login To Continue with the payment")
                return HttpResponseRedirect('/login_up/')

        else:
            messages.warning(request,'Password do not match')
            return HttpResponseRedirect('/sign/')
    return render(request,'integeration/register.html')




def login_up(request):
    if request.method=="POST":

        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        
        if user is not None: 
            login(request,user)
            messages.success(request,' you are logged in !! ')
            print(" successFully You are logged in")
            return HttpResponseRedirect('/profile/')
        else:
            messages.warning(request,' Invalid username and Password')
            return HttpResponseRedirect('/login_up/')

    return render(request,'integeration/login.html')

def success(request):
    print("we are in Success !!")
    if request.method=="POST":
        a=request.POST
        print(a)
    return render(request,'integeration/success.html')


@login_required(login_url='login_up')
def user_profile(request):
    return render(request,"integeration/profile.html")

# Create your views here.
