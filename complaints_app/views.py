from django.shortcuts import redirect, render
from .models import *
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request, "index.html")
def about(request):
    return render(request, "about.html")
def contact(request):
    return render(request, "contact.html")
def home(request):
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
