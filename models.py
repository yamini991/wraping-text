from django.db import models

# Create your models here.
class Job_seeker(models.Model):
    name= models.CharField(max_length=30)
    email= models.CharField(max_length=30)
    phone_no= models.CharField(max_length=15)
    skills=models.CharField(max_length=100)
    
    
    def __str__(self):
        return self.name+'-'+self.email+'-'+self.phone_no+'-'+self.skills