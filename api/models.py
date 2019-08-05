from django.db import models
from django.utils.text import slugify

# Create your models here.

class Contact(models.Model):
    number = models.IntegerField()
    mail = models.CharField(max_length=100)
    adress = models.CharField(max_length=100)

    def __str__(self):
        return self.mail



#class SosialLink(models.Model):
 #   facebook = models.URLField(max_length=100, blank=True, null=True)
  #  twiiter = models.URLField(max_length=100, blank=True, null=True)
   # instagram = models.URLField(max_length=100, blank=True, null=True)
    #linkedin = models.URLField(max_length=100, blank=True, null=True)
    #jobsid = models.ForeignKey('Jobs', on_delete=models.CASCADE, related_name = 'sosialid', blank=True, null=True)




class JobType(models.Model):
    name = models.CharField(max_length=100)
   
    def __str__(self):
        return self.name

class JobCategory(models.Model):
    name = models.CharField(max_length=100)


    def __str__(self):
        return self.name


		
class Jobs(models.Model):
    facebook = models.URLField(max_length=100, blank=True, null=True)
    twiiter = models.URLField(max_length=100, blank=True, null=True)
    instagram = models.URLField(max_length=100, blank=True, null=True)
    linkedin = models.URLField(max_length=100, blank=True, null=True)

    jobtype = models.ForeignKey(JobType, on_delete=models.CASCADE)
    jobcategory = models.ForeignKey(JobCategory, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='images/')
    companyname = models.CharField(max_length=100)
    jobname = models.CharField(max_length=100)
    jobdesj = models.TextField()
    position = models.IntegerField(default=0)
    experience = models.CharField(max_length=100)
    adress = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    website = models.URLField(max_length=100)
    number = models.CharField(max_length=100)
    salary = models.CharField(max_length=100)
    jobresponsibilities = models.TextField()
    jobskillrequirement = models.TextField()
    endtime = models.DateTimeField()
    start_time = models.DateTimeField(auto_now_add=True)
    jobsqualification = models.TextField()
    region = models.CharField(max_length=100, blank=True, null=True)


    def __str__(self):
        return self.jobname			

def images(instance, filename):
    filename = instance.slug + '.' + filename.split('.')[1]
    return "{0}/{1}".format(instance.slug, filname)


class DropMail(models.Model):
    adress = models.CharField(max_length=100)
    mail = models.CharField(max_length=100)
    number = models.IntegerField()

    def __str__(self):
        return self.mail

