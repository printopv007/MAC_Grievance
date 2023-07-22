from django.db import models

# Create your models here.
class MacGrievance(models.Model): #add complaints table for students
    subject=models.CharField(max_length=250) #grievance subject
    grievance_type=models.CharField(max_length=200) #grievance type
    grievance_description=models.TextField()  #grievance description
    
    
    
    def __str__(self):
        return self.subject
    
