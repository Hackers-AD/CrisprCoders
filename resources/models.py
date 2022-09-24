from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dob = models.DateField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    phone = models.PositiveBigIntegerField(blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    languages = models.TextField(blank=True, null=True)
    maritial_status = models.CharField(max_length=100, blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)

class Education(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    degree = models.CharField(max_length=255)
    college = models.CharField(max_length=255)
    gpa = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)
    specialization = models.CharField(max_length=255, blank=True, null=True)
    start_year = models.CharField(max_length=4, blank=True, null=True)
    end_year = models.CharField(max_length=4)

class Skill(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    skill = models.TextField(blank=True, null=True) 

class SkillFluency(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    fluency = models.PositiveIntegerField()

class Experience(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    designation = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    company_website = models.URLField(blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField()

class AcademicProject(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
