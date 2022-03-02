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
