import datetime
from django.db import models
from django.core.validators import MaxValueValidator
from c_auth.models import User
from primary_data.models import *
from employer.models import Profile as EmployerProfile
from app.choices import *
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=200)
    gender = models.CharField(
        max_length=1, choices=GENDER_CHOICES, null=True, blank=True)
    marital_status = models.CharField(
        max_length=1, choices=MARITAL_CHOICES, null=True, blank=True)
    birth_date = models.DateField("Date of Birth", null=True, blank=True)
    contact_number = models.CharField(max_length=10, null=True, blank=True)
    contact_verified = models.BooleanField(default=False)
    resume_file = models.FileField(upload_to='resume/', blank=True, null=True)
    profile_pic = models.FileField(upload_to='profile/', blank=True, null=True)
    resume_headline = models.TextField(null=True, blank=True)
    profile_summary = models.TextField(null=True, blank=True)
    aadhar_number = models.PositiveBigIntegerField(
        validators=[MaxValueValidator(999999999999)], blank=True, null=True, unique=True)
    aadhar_verified = models.BooleanField(default=False)
    pan_number = models.CharField(
        max_length=10, blank=True, null=True, unique=True)
    pan_verified = models.BooleanField(default=False)
    annual_salary_in_lac = models.PositiveIntegerField(
        validators=[MaxValueValidator(999)], choices=LAC_CHOICES, null=True, blank=True)
    annual_salary_in_thousand = models.PositiveIntegerField(
        validators=[MaxValueValidator(999)], choices=THOUSAND_CHOICES, null=True, blank=True)
    annual_salary = models.PositiveBigIntegerField(
        validators=[MaxValueValidator(9999999)], blank=True, null=True, unique=True)
    linked_in_profile = models.URLField(blank=True, null=True)
    twitter_profile = models.URLField(blank=True, null=True)
    youtube_profile = models.URLField(blank=True, null=True)
    facebook_profile = models.URLField(blank=True, null=True)
    instagram_profile = models.URLField(blank=True, null=True)
    webpage_link = models.URLField(blank=True, null=True)
    other_link = models.URLField(blank=True, null=True)
    follow = models.ManyToManyField(EmployerProfile, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    complete_profile_percentage = models.IntegerField(
        validators=[MaxValueValidator(999)], blank=True, null=True)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.email


class Employment(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=200)
    website_link = models.URLField(blank=True, null=True)
    employment_type = models.CharField(
        max_length=1, choices=EMPLOYMENT_CHOICES, null=True, blank=True)
    join_date = models.DateField(null=True, blank=True)
    leave_date = models.DateField(null=True, blank=True)
    designation = models.ForeignKey(Designation, on_delete=models.CASCADE)
    skill = models.ManyToManyField(KeySkill)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.profile.user.email


class CareerProfile(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    desired_Job_type = models.CharField(
        max_length=1, choices=DESIRED_JOB_CHOICES, null=True, blank=True)
    desired_employment_type = models.CharField(
        max_length=1, choices=EMPLOYMENT_CHOICES, null=True, blank=True)
    preferred_shift = models.CharField(
        max_length=1, choices=PREFERRED_SHIFT_CHOICES, null=True, blank=True)
    functional_area = models.ForeignKey(
        FunctionalArea, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    preferred_location = models.ForeignKey(
        PreferredLocation, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.profile.user.email


class Project(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    project_title = models.CharField(max_length=200)
    project_status = models.CharField(
        max_length=1, choices=STATUS_CHOICES, null=True, blank=True)
    project_start_year = models.IntegerField(
        choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    project_end_year = models.IntegerField(
        choices=YEAR_CHOICES, blank=True, null=True)
    project_description = models.TextField(null=True, blank=True)
    project_link = models.URLField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.profile.user.email


class Certification(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    certification_name = models.CharField(max_length=200)
    certified_by = models.CharField(max_length=200)
    certified_year = models.IntegerField(
        choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    certificate_link = models.URLField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.profile.user.email


class PaperResearchPublication(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    web_link = models.URLField(blank=True, null=True)
    published_year = models.IntegerField(
        choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    description = models.TextField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.profile.user.email


class WorkSample(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    web_link = models.URLField(blank=True, null=True)
    start_year = models.IntegerField(
        choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    end_year = models.IntegerField(choices=YEAR_CHOICES, null=True, blank=True)
    status = models.CharField(
        max_length=1, choices=STATUS_CHOICES, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.profile.user.email


class KnownLanguage(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    can_read = models.BooleanField(default=False)
    can_write = models.BooleanField(default=False)
    can_speak = models.BooleanField(default=False)
    proficiency = models.CharField(
        max_length=1, choices=PROFICIENCY_CHOICES, null=True, blank=True)

    def __str__(self):
        return self.profile.user.email
