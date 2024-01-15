from django.conf import settings
from django.db import models

def upload_student_image(instance, filename):
    return "students/{firstname}/{filename}".format(firstname=instance.firstname, filename=filename)

class Students(models.Model):
    firstname            = models.CharField(max_length=255, blank=True, null=True)
    lastname             = models.CharField(max_length=255, blank=True, null=True)
    dob                  = models.CharField(max_length=255, blank=True, null=True)
    gender               = models.CharField(max_length=255, blank=True, null=True)
    location             = models.CharField(max_length=255, blank=True, null=True)
    digitalAddress       = models.CharField(max_length=255, blank=True, null=True)
    contact              = models.CharField(max_length=255, blank=True, null=True)
    program_offered      = models.CharField(max_length=255, blank=True, null=True)
    department           = models.CharField(max_length=255, blank=True, null=True)
    year_of_admission    = models.CharField(max_length=255, blank=True, null=True)
    year_of_completion   = models.CharField(max_length=255, blank=True, null=True)
    description          = models.TextField(max_length=500, blank=True, null=True)
    image                = models.ImageField(upload_to=upload_student_image, blank=True, null=True)
    timestamp            = models.DateTimeField(auto_now_add=True)


    def __str__(self):
     return self.content or ""