from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login,logout as auth_logout



def signup(request):
    if request.method=='POST':
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        username=request.POST['Username']
        password=request.POST['password']
        cpassword=request.POST['cpassword']

        if password != cpassword:
            messages.error(request,"Confirm password did not match.")
            return redirect('/signup')
        else:
            user=User.objects.create_user(email=email,password=cpassword,first_name=fname,last_name=lname,username=username)
            user.save()
            messages.success(request,"Your account successfully created.")
            return redirect('/')
    else:
        return render(request,'signup.html')


def signin(request):
    if request.method == 'POST':
        username=request.POST['Username']
        cpassword=request.POST['cpassword']

        user = authenticate(request,username=username,password=cpassword)

        if user is not None:
            auth_login(request,user)
            messages.success(request,"Successfully signin.")
            return redirect('/')
        else:
            messages.error(request,"Somthing went wrong.")
            return redirect('/signin')

    return render(request,'signin.html')

def signout(request):
    auth_logout(request)
    messages.warning(request,"Logout successfully.")
    return redirect('/')