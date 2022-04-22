from django.db import models
from django.urls import reverse
from client.models import user
# Create your models here.

class canada_pr(models.Model):
    choice1=(
        ('Current skilled employment in New Zealand for 12 months or more (60 Points)','Current skilled employment in New Zealand for 12 months or more (60 Points)'),
        ('Offer of skilled employment in New Zealand or current skilled employment in New Zealand for less than 12 months (50 Points)', 'Offer of skilled employment in New Zealand or current skilled employment in New Zealand for less than 12 months (50 Points)')
    )
    SKILLED_EMPLOYMENT=models.CharField(max_length=200, choices=choice1)
    choice2=(
        ('2 Years (10 Points)','2 Years (10 Points)'),
        ('4 Years (15 Points)','4 Years (15 Points)'),
        ('6 Years (20 Points)', '6 Years (20 Points)'),
        ('8 Years (25 Points)', '8 Years (25 Points)'),
        ('10 Years (30 Points)', '10 Years (30 Points)'),
    )
    WORK_EXPERIENCE=models.CharField(max_length=200, choices=choice2)
    choice3=(
        ('Recognised basic qualification (e.g. trade qualification, diploma, bachelors degree, bachelors degree with Honours) (50 Points)','Recognised basic qualification (e.g. trade qualification, diploma, bachelors degree, bachelors degree with Honours) (50 Points)'),
        ('Recognised post-graduate qualification (Masters degree, Doctorate) (55 Points)','Recognised post-graduate qualification (Masters degree, Doctorate) (55 Points)')
    )
    QUALIFICATIONS=models.CharField(max_length=200, choices=choice3)
    choice4=(
        ('20-29 (30 Points)','20-29 (30 Points)'),
        ('30-39 (25 Points)','30-39 (25 Points)'),
        ('40-44 (20 Points)', '40-44 (20 Points)'),
        ('45-49 (10 Points)', '45-49 (10 Points)'),
        ('50-55 (5 Points)', '50-55 (5 Points)')
    )
    AGE_20TO55_YEARS=models.CharField(max_length=200, choices=choice4)
    choice5=(
        ('An identified future growth area, identified cluster, area of absolute skills shortage (5 Points)','An identified future growth area, identified cluster, area of absolute skills shortage (5 Points)'),
        ('Region outside Auckland (10 Points)','Region outside Auckland (10 Points)'),
        ('Partner employment or offer of employment (10 Points)','Partner employment or offer of employment (10 Points)')
    )
    Skilled_employment_2=models.CharField(max_length=200,choices=choice5)
    choice6=(
        ('2 Years (5 Points)','2 Years (5 Points)'),
        ('4 Years (10 Points)','4 Years (10 Points)'),
        ('6 Years (15 Points)','6 Years (15 Points)')
    )
    Work_experience_2=models.CharField(max_length=200,choices=choice6)
    choice7=(
        ('2 to 5 years (5 Points)','2 to 5 years (5 Points)'),
        ('6 years or more (10 Points)','6 years or more (10 Points)')
    )
    Additional_Bonus_Points=models.CharField(max_length=200, choices=choice7)
    choice8=(
        ('Recognised New Zealand qualification (and at least two years study in NZ) (10 Points)','Recognised New Zealand qualification (and at least two years study in NZ) (10 Points)'),
        ('Qualification in an identified future growth area, cluster or area of absolute skill shortage (5 Points)','Qualification in an identified future growth area, cluster or area of absolute skill shortage (5 Points)')
    )
    Qualifications=models.CharField(max_length=200, choices=choice8)
    choice9=(
        ('None','None'),
        ('Partner Qualifications (10 Points)','Partner Qualifications (10 Points)')
    )
    Partner_Qualifications=models.CharField(max_length=200, choices=choice9)
    client=models.ForeignKey(user,on_delete=models.CASCADE, related_name='canada_pr', blank=True,null=True)
    text=models.TextField(max_length=50)
    city=models.CharField(max_length=100)
    resume=models.FileField(default="",upload_to="profile", blank=True,null=True)

    def __str__(self):
        return f"{self.SKILLED_EMPLOYMENT}"

    def get_absolute_url(self):
        return reverse('canada_pr-view')
