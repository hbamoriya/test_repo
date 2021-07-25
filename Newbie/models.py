from django.db import models
import datetime
from django.utils import timezone

class Allcourses(models.Model):
    coursesname=models.CharField(max_length = 200)
    insname =models.CharField(max_length = 300)
    startedfrom = models.DateTimeField('started From')
    #Channel_img =models.ImageField(upload_to='images/')

    def __str__(self):
        return self.coursesname

    def was_published_recently(self, startedfrom=None):
        return self.startedfrom >= timezone.now() - datetime.timedelta(days=1)

class details(models.Model):
    course = models.ForeignKey(Allcourses,on_delete=models.CASCADE)
    #sp = models.CharField(max_length = 500)
    #il = models.CharField(max_length = 500)
    ct = models.CharField(max_length=500)
    Your_choice = models.BooleanField(default=False)

    def __str__(self):
        return str(self.ct)
