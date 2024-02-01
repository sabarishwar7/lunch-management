from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from . import models
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User,auth
from django.contrib import auth,messages
from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib.auth import authenticate,login,logout
from datetime import datetime,timedelta,date
from django.core.mail import send_mail
# Create your views here.

def register_view(request):
    
    if request.method == 'POST':
        username=request.POST['username']
        e_id=request.POST['e_id']
        email = request.POST['email']
        password1 = request.POST['password']
           
        if (User.objects.filter(email=email).exists()):
             messages.info(request,"User Already Exists")
             return HttpResponseRedirect('login')
             
             
        else:
             user = User.objects.create_user(first_name=username,email=email,password=password1)
             tkn_no=new_plt_no(user.id)
             user = User.objects.create_user(Token_no=tkn_no)
             user.save()
             return HttpResponseRedirect('profile')
    
        
               
           
    return render(request, 'order/register.html')

def new_plt_no(id):
                if True:
                    pt_no=str('T')+str(id)
                    return pt_no

def login_view(request):
    if request=='POST':
        e_id=e_id
        password=password
        user= auth.authenticate(e_id=e_id,password=password)
        if user is not None:
             auth.login(request,user)
             return redirect('food')
             
        else:
             messages.info(request,'Invalid values')

    return render(request,"order/login.html")

        


def logout_view(request):
    
    return render(request, "order/logout.html")


def forgotpass_view(request):
    return render(request)

login_required(login_url='login')
def profile_view(request):
    user=models.detail.objects.all()

    return render(request,"order/profile.html")

def navuser_view(request):
    return render(request)

def navadmin_view(request):
    return render(request)

login_required(login_url='login')
def food_view(request):
    return render(request,"order/food.html")

login_required(login_url='login')
def snack_view(request):
    return render(request,"order/snack.html")

login_required(login_url='login')
def drink_view(request):
    return render(request,"order/drink.html")

login_required(login_url='login')
def addmenu_view(request):
    if request=='POST':
         name=request.POST['name']
         menu=request.POST['menu']
         dish=(menu,name)
         models.Dish.objects.all(**dish)
         dish.save()
    
    return render(request,"order/addmenu.html")


def order_view(request) :
     order=models.Order.objects.all()
     li=[]
     for i in order:
          dish=list(models.Order.objects.filter(tkn_no=i.tkn_no))
          user=list(models.detail.objects.all())
          j=0
          for y in dish:
               t=(dish[j].tkn_no,dish[j].customer,dish[j].food,dish[j].order_date,dish[j].order_time)
               j=j+1
               li.append(t)
     return render(request,"order/view.html")