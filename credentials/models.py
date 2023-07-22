# from django.db import models
# from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
# from django.db.models.fields.related import ForeignKey, OneToOneField

# class UserManager(BaseUserManager):

#     def create_user(self,first_name,last_name,username,email,password=None):
#         if not email:
#             raise ValueError('Please provide a valid email address')
#         if not username:
#             raise ValueError('Please provide a valid username')
        
#         user=self.model(
#             email=self.normalize_email(email),
#             username=username,
#             first_name=first_name,
#             last_name=last_name,
#         )
#         user.set_password(password)
#         user.save(using=self.db)
#         return user
#     def create_SuperUser(self,first_name,last_name,username,email,password=None):
#         user=self.create_User(
#              email=self.normalize_email(email),
#             username=username,
#             first_name=first_name,
#             last_name=last_name,
#         )
#         user.is_admin=True
#         user.is_active=True
#         user.is_staff=True
#         user.is_superadmin=True
#         user.save(using=self.db)
#         return user

# class User(AbstractBaseUser):
#     STUDENT=1
#     ADMIN=2
#     ROLE_CHOICE=(
#         (STUDENT,'Student'),
#         (ADMIN,'Admin'),
#     )
#     first_name=models.CharField(max_length=100)
#     last_name=models.CharField(max_length=100)
#     username=models.CharField(max_length=100, unique=True)
#     email=models.EmailField(max_length=100, unique=True)
#     department=models.CharField(max_length=50)
#     course=models.CharField(max_length=50)
#     phone_number=models.CharField(max_length=150,blank=True,null=True)
#     role=models.PositiveSmallIntegerField(choices=ROLE_CHOICE,blank=True,null=True)

#     date_joined=models.DateField(auto_now_add=True)
#     last_login=models.DateField(auto_now_add=True)
#     created_date=models.DateField(auto_now_add=True)
#     modified_date=models.DateField(auto_now_add=True)
#     is_admin=models.BooleanField(default=False)
#     is_staff=models.BooleanField(default=False)
#     is_active=models.BooleanField(default=False)
#     is_superadmin=models.BooleanField(default=False)

#     USERNAME_FIELD ='email'
#     REQUIRED_FIELDS = ['username','password']


# from django.db import models
# from django.contrib.auth.models import AbstractUser 
# from django.contrib.auth.models import AbstractBaseUser
# # Create your models here.



# class Department_Admin(AbstractBaseUser):
    
#     username = models.CharField(max_length=150, unique=True)
#     password = models.CharField(max_length=128)
#     department = models.CharField(max_length=100)
#     phone_number=models.CharField(max_length=100)
#     course=models.CharField(max_length=250)
#     email=models.EmailField()


#     # Other fields specific to Department Admin model

#     def __str__(self):
#         return self.username

# class User(AbstractBaseUser):
#     id=models.AutoField(primary_key=True)
#     first_name = models.CharField(max_length=150)
#     last_name = models.CharField(max_length=150)
#     email = models.EmailField()
#     username =models.CharField(max_length=100,unique=True)
#     password = models.CharField(max_length=128)
#     phone_no =models.CharField(max_length=100,unique=True) 
#     course =models.CharField(max_length=150)
#     department=models.CharField(max_length=150)
    

#     def __str__(self):
#         return self.username

# class Worker(AbstractBaseUser):
    
#     first_name = models.CharField(max_length=150)
#     last_name = models.CharField(max_length=150)
#     email = models.EmailField()
#     username =models.CharField(max_length=100,unique=True)
#     password = models.CharField(max_length=128)
#     phone_no =models.CharField(max_length=100,unique=True)
#     location =models.CharField(max_length=150)
#     user_image =models.ImageField(upload_to="workerProfile") 
#     dob =models.DateField(null=True)
#     user_bio=models.CharField(max_length=150)
#     type=models.CharField(max_length=100,default='worker') 
#     address=models.CharField(max_length=300)
    
#     job_title=models.CharField(max_length=150,null= True)
#     catagory=models.CharField(max_length=150,null= True)
#     experience=models.CharField(max_length=150,null= True)
#     skill_1 =models.CharField(max_length=150,null= True)
#     skill_2 =models.CharField(max_length=150,null= True)
#     skill_3 =models.CharField(max_length=150,null= True)
#     id_proof=models.ImageField(upload_to="workerfile")
#     exp_proof=models.ImageField(upload_to="workerfile")
#     cv=models.ImageField(upload_to="workerfile")

#     is_approved=models.BooleanField(null= True)
#     status=models.BooleanField(null= True)
#     report=models.BooleanField(null= True)

#     def __str__(self):
#         return self.username

# class login(models.Model):
#     username =models.CharField(max_length=100)
#     password = models.CharField(max_length=128)
    
#     def __str__(self):
#         return self.username


