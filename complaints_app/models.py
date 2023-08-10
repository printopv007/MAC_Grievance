from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your models here.
#add grievance model
class MacGrievance(models.Model): #add complaints table for students
    name=models.CharField(max_length=100) #username for students
    subject=models.CharField(max_length=250) #grievance subject
    COURSE=(('MCA',"MCA"),('MBA',"MBA"),('MSC',"MSC")) #student COURSE
    TYPE=(('ClassRoom',"ClassRoom"),('Teacher',"Teacher"),('Management',"Management"),('College',"College"),('Other',"Other")) #grievance type
    grievance_description=models.TextField()  #grievance description    
    grievance_type=models.CharField(choices=TYPE,null=True,max_length=200)
    course=models.CharField(choices=COURSE,null=True,max_length=200)
    def __str__(self):
        return self.subject

#feedback model  
class Feedback(models.Model):
    name=models.CharField(max_length=100) #username for students
    feed_sub=models.CharField(max_length=100) #feedback subject
    feed_description=models.TextField() #feedback description

    def __str__(self):
        return self.feed_sub