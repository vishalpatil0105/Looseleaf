from django.db import models
from django.db.models import Max
# Create your models here.


# Student Model
class Students(models.Model):
    # student_id = models.CharField(primary_key=True, editable=False, max_length=50)
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    roll_no = models.IntegerField()
    standard = models.IntegerField(null=False)

    def __str__(self):
        return self.first_name


# Course Model
class Courses(models.Model):
    # course_id = models.CharField(primary_key=True, editable=False, max_length=50)
    id = models.AutoField(primary_key=True)
    course_name = models.CharField(max_length=200, null=False)
    standard = models.IntegerField(null=False)
    is_compulsory = models.BooleanField(null=False, default=False)
    # student_id = models.CharField(max_length=60,null=False)
    student_id = models.ForeignKey(Students, on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return self.course_name


