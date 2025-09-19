from django.db import models

# Create your models here.



class Information(models.Model):
    phone = models.IntegerField(max_length=11, null=True)
    email = models.EmailField(null=True)