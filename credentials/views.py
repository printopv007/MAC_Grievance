from django.forms import ValidationError
from django.contrib import messages, auth
from django.shortcuts import redirect, render
from django.contrib.auth.models import User


# Create your views here.
def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.info(request, "Invalid details!")
            return redirect('login')
    return render(request, "login.html")


def logout(request):
    auth.logout(request)
    return redirect('/')

def register(request):
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['firstname']
        lname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password1']
        


        if password == password1 and not email.endswith('@macfast.ac.in'):
             messages.info(request,"Only macfast.ac.in email addresses are allowed or Password does not match")
             return redirect('register')
        elif User.objects.filter(username=username).exists():
                messages.info(request, "Username already Exists")
                return redirect('register')
        elif User.objects.filter(email=email).exists():
                messages.info(request, "Email already Exists")
                return redirect('register')
        else:
                user = User.objects.create_user(username=username, first_name=fname, last_name=lname, email=email,
                                                password=password)
                user.save();
                messages.info(request, "User Successfully Created!")
                return render(request, "login.html")

        return redirect('/')
    return render(request, "register.html")