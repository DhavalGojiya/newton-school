from django.db import models


# Create your models here.
class School(models.Model):
    DATA_CHOICE = [('A', 'Good Institute'),
                   ('B', 'Average Institute'),
                   ('C', 'Very Poor Institute')
                   ]
    institute_name = models.CharField(max_length=44)
    established_year = models.IntegerField()
    owner_name = models.CharField(max_length=25)
    address = models.TextField(max_length=100)
    rating = models.CharField(max_length=5, choices=DATA_CHOICE)
