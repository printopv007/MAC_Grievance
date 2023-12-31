from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your models here.
#add grievance model
class MacGrievance(models.Model): #add complaints table for students
    name=models.CharField(max_length=100) #username for students
    subject=models.CharField(max_length=250) #grievance subject
    STATUS =(("Solved",'Solved'),("InProgress", 'InProgress'),("Pending",'Pending'),("Unsolved", 'Unsolved'))
    TYPE=(('ClassRoom',"ClassRoom"),('Teacher',"Teacher"),('Management',"Management"),('College',"College"),('Other',"Other")) #grievance type
    grievance_description=models.TextField()  #grievance description    
    grievance_type=models.CharField(choices=TYPE,null=True,max_length=200)
    department=models.CharField(max_length=200)
    status=models.CharField(choices=STATUS,default="Pending",max_length=100)
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.subject

#feedback model  
class Feedback(models.Model):
    name=models.CharField(max_length=100) #username for students
    feed_sub=models.CharField(max_length=100) #feedback subject
    feed_description=models.TextField() #feedback description
    department=models.CharField(max_length=200) #department
    def __str__(self):
        return self.feed_sub
    
