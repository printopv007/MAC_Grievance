from django.shortcuts import redirect, render
from .models import *
from django.contrib import messages
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your views here.
def index(request):
    return render(request, "index.html")
def about(request):
    return render(request, "about.html")
def contact(request):
    return render(request, "contact.html")
def home(request):
    # username=request.session.get('username')
    # users=User.objects.all()
    # for i in users:
    #     if i.username == username:
    #        email=i.email
    # user=User.objects.get(username=username)
    # complaints=MacGrievance.objects.filter(id=id)
    # context={"username": username,"email":email, "complaints":complaints }
    return render(request, "home.html")

def add(request):
    if request.method == "POST":
        subject = request.POST['subject']
        grievance_type = request.POST['grievance_type']
        grievance_description = request.POST['grievance_description']
        MacGrievance.objects.create(subject=subject,
                                     grievance_type=grievance_type, 
                                     grievance_description=grievance_description)  
        MacGrievance(subject=subject, grievance_description=grievance_description, grievance_type=grievance_type)
        messages.info(request,'Successfully Added your Complaint')
        return redirect('add')
    
    return render(request, 'add.html')

def view(request):
    queryset=MacGrievance.objects.all()
    context={'grievance':queryset}
    return render(request, 'view.html',context)

def feed(request):
    if request.method == "POST":
        feed_sub = request.POST['feed_sub']
        feed_description = request.POST['feed_description']
        MacGrievance.objects.create(subject=subject,
                                     grievance_type=grievance_type, 
                                     grievance_description=grievance_description)  
        MacGrievance(subject=subject, grievance_description=grievance_description, grievance_type=grievance_type)
        messages.info(request,'Successfully Added your Complaint')
        return redirect('add')