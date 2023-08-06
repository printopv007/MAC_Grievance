from django.forms import ValidationError
from django.contrib import messages, auth
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User = get_user_model()
from django.contrib.auth import login as auth_login
# Create your views here.
def login1(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        password1 = request.POST['password1']
        user =auth.authenticate(username=username, password=password)
        if user is not None and password==password1 and isinstance(user, User):
            auth.login(request, user)
            return _extracted_from_login_view_21(request, user, 'home')
            # return redirect('home')
        
        else:
            messages.info(request, "Invalid details!")
            return redirect('login1')
    return render(request, "login.html")

# TODO Rename this here and in `login_view`
def _extracted_from_login_view_21(request, user, arg2):
    auth.login(request, user)
    request.session['username'] = request.user.username
    request.session['id'] = request.user.id
    return redirect(arg2)



def logout(request):
    auth.logout(request)
    return redirect('login1')

def register(request):
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['firstname']
        lname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password1']
        department = request.POST['department']
        phone_number = request.POST['number']


        if not email.endswith('@macfast.ac.in'):
             messages.info(request,"Only macfast.ac.in email addresses are allowed")
             return redirect('register')
        elif password != password1:
             messages.info(request,"Password mismatch")
             return redirect('register')
             
        elif User.objects.filter(username=username).exists():
                messages.info(request, "Username already Exists")
                return redirect('register')
        elif User.objects.filter(email=email).exists():
                messages.info(request, "Email already Exists")
                return redirect('register')
        else:
                user = User.objects.create_user(username=username, first_name=fname, last_name=lname, email=email,
                                                password=password,department=department,phone_number=phone_number)
                user.save();
                messages.info(request, "User Successfully Created!")
                return render(request, "login.html")

        #return redirect('/')
    return render(request, "register.html")