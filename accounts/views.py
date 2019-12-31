from django.shortcuts import render , redirect
from django.contrib import messages
from django.contrib.auth.models import User , auth

# Create your views here.

def register(request):
    if request.method=="POST":
        usernameF=request.POST.get('usernamef!',False)  
        firstF=request.POST.get('f1',False)  
        last_nameF=request.POST.get('l1',False)  
        password1F=request.POST.get('pf1',False)  
        password2F=request.POST.get('p2',False) 
        emailF=request.POST.get('email!',False)  
        if password1F==password2F:
            if User.objects.filter(username=usernameF).exists():
                messages.info(request,'Username Taken')
                return redirect('register')
            elif User.objects.filter(email=emailF).exists():
                messages.info(request,'Email Taken')
                return redirect('register')
            else:
                user=User.objects.create_user(username=usernameF,password=password1F,email=emailF,first_name=firstF,last_name=last_nameF)
                user.save();
                print('user created')
                return redirect('login')
        else:
            print('Password not matching')
            return redirect('register')
    else:
        return render(request,'register.html')
def login(request):
    if request.method=="POST":
        usernameF2=request.POST.get('usernamef!',False)
        password1F2=request.POST.get('pf1',False)
        user=auth.authenticate(username=usernameF2,password=password1F2)
        if user is not None:
            auth.login(request,user)
            print ('Logined user')
            return redirect('/')
        else :
            messages.info(request,'invalid credentials')
            return redirect('login')
    else:
        return render(request,'login.html')
    

        
 