from django.db import models
from django.urls import reverse

from django.contrib.auth.models import User

class Project(models.Model):
    name = models.CharField(max_length=60)
    description = models.CharField(max_length=250)

    def get_absolute_url(self):
        return reverse('account:project-list')

    def __str__(self):
        return (self.name)

class Skill(models.Model):
    name = models.CharField(max_length=60)

    def get_absolute_url(self):
        return reverse('account:skill-list')

    def __str__(self):
        return (self.name)

class Role(models.Model):
    name = models.CharField(max_length=60)

    def get_absolute_url(self):
        return reverse('account:role-list')

    def __str__(self):
        return (self.name)

class ProfileImage(models.Model):
    image = models.FileField(upload_to='profile/', blank=True)

    def display_text_file(self):
        with open(self.image.path) as fp:
            return fp.read().replace('\n', '<br>')

    def get_absolute_url(self):
        return reverse('account:profile-image-upload')

    def __str__(self):
        return (self.name)

class Report(models.Model):
    name = models.CharField(max_length=250)

    def get_absolute_url(self):
        return reverse('account:report-list')

    def __str__(self):
        return (self.name)

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    employee_id = models.CharField(max_length=15)
    manager = models.ForeignKey("Employee",null=True,blank=True)
    date_of_birth= models.DateField()
    date_of_joining = models.DateField()
    role = models.ForeignKey(Role,max_length=16,null=True, blank=True )
    pan_number = models.CharField(max_length=255)
    bank_account_number = models.CharField(max_length=255)
    emergency_contact_number = models.CharField(max_length=11)
    project = models.ForeignKey(Project, null=True, blank=True)
    skill = models.ManyToManyField(Skill)
    image = models.FileField(upload_to='profile/',null=True, blank=True)

    def get_absolute_url(self):
        return reverse('account:home')

    def __str__(self):
         return (self.user.first_name+ " "+self.user.last_name)



class Document(models.Model):
    docfile = models.FileField(upload_to='documents/',blank=True)
    description = models.CharField(max_length=255, blank=True)
    employee = models.ForeignKey(Employee)

    def get_absolute_url(self):
        return reverse('account:home')

    def __str__(self):
        return str(self.docfile)


