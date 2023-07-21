from django.db import models

# Create your models here.
class MacGrievance(models.Model):
    subject=models.CharField(max_length=250) #grievance subject
    grievance_description=models.TextField()  #grievance description
    grievance_type=models.CharField(max_length=200) #grievance type
    