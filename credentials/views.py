from django.forms import ValidationError
from django.contrib import messages, auth
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your views here.
def login1(request):
    if request.method == "POST":
        username = request.POST['username']
        department=request.POST['department']
        password = request.POST['password']
        password1 = request.POST['password1']
        user =auth.authenticate(username=username, password=password, department=department)
        if user is not None and password==password1 and isinstance(user, User):
            auth.login(request, user)
            request.session['username'] = user.username
            request.session['department'] = user.department
            return _extracted_from_login_view_21(request, user, 'home')
            
        else:
            messages.info(request, "Invalid details!")
            return render(request,'login.html')
    return render(request, "login.html")

# TODO Rename this here and in `login_view`
def _extracted_from_login_view_21(request, user, arg2):
    auth.login(request, user)
    request.session['username'] = request.user.username
    request.session['id'] = request.user.id
    request.session['department'] =request.user.department
    return redirect(arg2)



def logout(request):
    auth.logout(request)
    return redirect('/credentials/login1')

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
             return redirect('/credentials/register')
        elif password != password1:
             messages.info(request,"Password mismatch")
             return redirect('/credentials/register')
             
        elif User.objects.filter(username=username).exists():
                messages.info(request, "Username already Exists")
                return redirect('/credentials/register')
        elif User.objects.filter(email=email).exists():
                messages.info(request, "Email already Exists")
                return redirect('/credentials/register')
        else:
                user = User.objects.create_user(username=username, first_name=fname, last_name=lname, email=email,
                                                password=password,department=department,phone_number=phone_number)

                user.save();
                

                messages.info(request, "User Successfully Created!")
                return redirect('/credentials/login1')

        #return redirect('/')
    return render(request, "register.html")

def admin_login(request):
    error = ""
    if request.method == "POST":
        username =request.POST['username']
        password =request.POST['password']
        user =auth.authenticate(username=username, password=password)
        try:
            if user.is_staff:
                auth.login(request,user)
                request.session['username'] = user.username
                error ="no"
            else:
                error="yes"
        except:
            error="yes"
    d={'error':error}        
    return render(request,"admin_login.html",d)

def admin_home(request):
     return render(request,'admin_home.html')

def admin_logout(request):
     auth.logout(request)
     return redirect('/credentials/login1/')

def add_user(request):
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
             return redirect('add_user')
        elif password != password1:
             messages.info(request,"Password mismatch")
             return redirect('add_user')
             
        elif User.objects.filter(username=username).exists():
                messages.info(request, "Username already Exists")
                return redirect('add_user')
        elif User.objects.filter(email=email).exists():
                messages.info(request, "Email already Exists")
                return redirect('add_user')
        else:
                user = User.objects.create_user(username=username, first_name=fname, last_name=lname, email=email,
                                                password=password,department=department,phone_number=phone_number)
                user.save();
                messages.info(request, "User Successfully Added!")
                return redirect( '/credentials/add_user')
    return render(request, "add_user.html")


def sadd_user(request):
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
             return redirect('sadd_user')
        elif password != password1:
             messages.info(request,"Password mismatch")
             return redirect('sadd_user')
             
        elif User.objects.filter(username=username).exists():
                messages.info(request, "Username already Exists")
                return redirect('sadd_user')
        elif User.objects.filter(email=email).exists():
                messages.info(request, "Email already Exists")
                return redirect('sadd_user')
        else:
                user = User.objects.create_user(username=username, first_name=fname, last_name=lname, email=email,
                                                password=password,department=department,phone_number=phone_number)
                user.save();
                messages.info(request, "User Successfully Added!")
                return redirect( '/credentials/sadd_user/')
    return render(request, "sadd_user.html")

def admin_manage_user(request):
    queryset = User.objects.all()
    context={'sadd_user': queryset}
    return render(request, "admin_manage_user.html",context)

def admin_delete_user(request, id):
    if request.method=='POST':
        user=User.objects.get(id=id)
        user.delete()
        return redirect('/credentials/admin_manage_user/')
    return render(request,"admin_delete_user.html") 

def dep_login(request):
    error = ""
    if request.method == "POST":
        username =request.POST['username']
        password =request.POST['password']
        user =auth.authenticate(username=username, password=password)
        try:
            if user.is_staff:
                auth.login(request,user)
                request.session['username'] = user.username
                error ="no"
            else:
                error="yes"
        except:
            error="yes"
    d={'error':error}        
    return render(request,"dep_login.html",d)


def dep_home(request):
     return render(request,"dep_home.html")
     

def dep_manage(request):
    username=request.session['username']
    queryset = User.objects.filter(department=username)
    context={'manage': queryset}
    return render(request, "dep_manage.html",context)

def dep_delete(request, id):

    if request.method=='POST':
        user=User.objects.get(id=id)
        user.delete()
        return redirect('/credentials/dep_manage/')
    return render(request,"dep_delete.html") 





def dep_logout(request):
      auth.logout(request)
      return redirect('/credentials/login1/')