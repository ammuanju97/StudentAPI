from django.contrib.auth.models import User
from django.db import models


# model for student profile
class StudentProfile(models.Model):

    def nameFile(instance, filename):
        return '/'.join(['Images', str(instance.user), filename])
        
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    image = models.ImageField(upload_to = nameFile, blank = True, default = 'None')
    DOB = models.DateField(max_length = 8, null = False, blank =False)
    address = models.TextField(null = False, blank = False)

    def __str__(self):
        return self.user.username


class StudentMarkDetails(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    english_mark = models.IntegerField(blank=True, null=True)
    maths_mark = models.IntegerField(blank=True, null=True)
    science_mark = models.IntegerField(blank=True, null=True)
    malayalam_mark = models.IntegerField(blank=True, null=True)
    total_mark = models.IntegerField(blank=True, null=True,)
    grand_total = models.IntegerField(blank=True, null=True, default = 400)
    percentage = models.IntegerField(blank=True, null=True)
    grade = models.CharField(max_length = 10, null=True, blank=True)
    final_result = models.CharField(max_length = 15, null=True, blank=True)

    def __str__(self):
        return self.user.username
