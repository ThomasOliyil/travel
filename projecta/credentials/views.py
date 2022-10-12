from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"Invalid user")
            return redirect('credentials:login')
    return render(request, "login.html")
def logout(request):
    auth.logout(request)
    return redirect('/')
def register(request):
    if request.method == 'POST':
        username = request.POST['u_name']
        firstname = request.POST['f_name']
        lastname = request.POST['l_name']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['c-password']

        if cpassword == password:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username already taken")
                return redirect('credentials:register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email already taken")
                return redirect('credentials:register')
            else:
                user = User.objects.create_user(username=username, first_name=firstname, last_name=lastname, password=password, email=email)
                user.save();
                return redirect('credentials:login')

        else:
            messages.info(request,"Password not matched")
            return redirect('credentials:register')
        return redirect('/')

    return render(request,"register.html")
