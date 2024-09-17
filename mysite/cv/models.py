from django.db import models
from django.utils import timezone
from datetime import date

class Personal_info(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    website = models.CharField(max_length=100)
    city_live_in = models.CharField(max_length=100)
    country_live_in = models.CharField(max_length=100)
    
    def __str__(self):
        return self.first_name


class Education(models.Model):
    personal_info = models.ForeignKey(Personal_info, on_delete=models.CASCADE)
    school_name = models.CharField(max_length=100)
    major = models.CharField(max_length=100,default='')
    degree = models.CharField(max_length=100)
    study_from = models.CharField(max_length=100)
    study_to = models.CharField(max_length=100)
    city_in = models.CharField(max_length=100)
    country_in = models.CharField(max_length=100)

class Work_experience(models.Model):
    personal_info = models.ForeignKey(Personal_info, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100)
    job_description = models.CharField(max_length=300)
    work_from = models.CharField(max_length=100)
    work_to = models.CharField(max_length=100)
    city_in = models.CharField(max_length=100)
    country_in = models.CharField(max_length=100)
    
class Skills(models.Model):
    personal_info = models.ForeignKey(Personal_info, on_delete=models.CASCADE)
    skill_name = models.CharField(max_length=100)
    skill_description = models.CharField(max_length=300)

