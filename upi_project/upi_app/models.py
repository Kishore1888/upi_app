from django.db import models

# Create your models here.
class login_form(models.Model):
    account_number=models.CharField(max_length=20)
    ifsc_code=models.CharField(max_length=15)
    name=models.CharField(max_length=10)
    branch_name=models.CharField(max_length=30)
    mobile_number=models.CharField(max_length=15)


    


   
  
   
