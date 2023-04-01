from django.db import models
from .choices import COURSE_TYPE_CHOICES


class Courses(models.Model):
    course_name = models.CharField(max_length=255)
    standard = models.IntegerField()
    course_description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    course_type = models.CharField(max_length=10, choices=COURSE_TYPE_CHOICES)
    price = models.IntegerField()
    teacher = models.ForeignKey('users.SchoolUser', on_delete=models.CASCADE)
