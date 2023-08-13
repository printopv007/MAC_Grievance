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
        username=request.session['username'] 
        department=request.session['department']
        #name=request.POST['username']
        subject = request.POST['subject']
        #course=request.POST['course']
        grievance_type = request.POST['grievance_type']
        grievance_description = request.POST['grievance_description']
        MacGrievance.objects.create(name=username,subject=subject,
                                     grievance_type=grievance_type, department=department,
                                     grievance_description=grievance_description)  
        MacGrievance(subject=subject, grievance_description=grievance_description, grievance_type=grievance_type)
        messages.info(request,'Successfully Added your Complaint')
        return redirect('add')
    
    return render(request, 'add.html')

def view(request):
    username=request.session['username']
    department=request.session['department']
    queryset=MacGrievance.objects.filter(name=username,department=department)
    context={'grievance':queryset}
    return render(request, 'view.html',context)

def feed(request):
    if request.method == "POST":
        username=request.session['username'] 
        department=request.session['department']
        feed_sub = request.POST['feed_sub']
        feed_description = request.POST['feed_description']
        Feedback.objects.create(name=username,department=department,feed_sub=feed_sub,
                                     feed_description=feed_description, 
                                    )  
        Feedback(feed_sub=feed_sub, feed_description=feed_description)
        messages.info(request,'Successfully Added your Feedback')
        return redirect('feed')
    return render(request, 'feed.html')


def admin_view(request): #All Grievance View  for Principal Admin
    queryset=MacGrievance.objects.all()
    context={'grievance':queryset}
    return render(request, 'admin_view.html',context)


def admin_feed_view(request): #All Feedback View for Principal Admin
    queryset=Feedback.objects.all()
    context={'feed':queryset}
    return render(request, 'admin_feed_view.html',context)

# def mca_view(request): #All Grievance View  for MCA Admin
#     username=request.session['username']
#     queryset=MacGrievance.objects.filter(department=username)
#     context={'mca':queryset}
#     return render(request, "mca_view.html",context)

# def mba_view(request): #All Grievance View  for MBA Admin
#     username=request.session['username']
#     queryset=MacGrievance.objects.filter(department=username)
#     context={'mba':queryset}
#     return render(request, "mba_view.html",context)

def dep_grieve_view(request): #All Grievance View  for MSC Admin
    username=request.session['username']
    queryset=MacGrievance.objects.filter(department=username)
    context={'grieve':queryset}
    return render(request,"dep_grieve_view.html",context)
    

def dep_feed_view(request):
    username=request.session['username']
    queryset=Feedback.objects.filter(department=username)
    context={'feed':queryset}
    return render(request, 'dep_feed_view.html',context)