from django.db import models
from django.core.validators import MaxValueValidator
from c_auth.models import User
from primary_data.models import *
from app.choices import *

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(
        User, related_name="%(app_label)s_%(class)s_user", on_delete=models.CASCADE,)
    full_name = models.CharField(max_length=200)
    gender = models.CharField(
        max_length=1, choices=GENDER_CHOICES, null=True, blank=True)
    birth_date = models.DateField("Date of Birth", null=True, blank=True)
    contact_number = models.CharField(max_length=10, null=True, blank=True)
    contact_verified = models.BooleanField(default=False)
    profile_pic = models.FileField(upload_to='profile/', blank=True, null=True)
    address_proof = models.FileField(
        upload_to='address/', blank=True, null=True)
    address_verified = models.BooleanField(default=False)
    aadhar_number = models.PositiveBigIntegerField(
        validators=[MaxValueValidator(999999999999)], blank=True, null=True, unique=True)
    aadhar_verified = models.BooleanField(default=False)
    pan_number = models.CharField(
        max_length=10, blank=True, null=True, unique=True)
    pan_verified = models.BooleanField(default=False)
    linked_in_profile = models.URLField(blank=True, null=True)
    twitter_profile = models.URLField(blank=True, null=True)
    youtube_profile = models.URLField(blank=True, null=True)
    facebook_profile = models.URLField(blank=True, null=True)
    instagram_profile = models.URLField(blank=True, null=True)
    webpage_link = models.URLField(blank=True, null=True)
    other_link = models.URLField(blank=True, null=True)
    complete_profile_percentage = models.IntegerField(
        validators=[MaxValueValidator(999)], blank=True, null=True)
    address = models.OneToOneField(Address, related_name="%(app_label)s_%(class)s_address", on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.email


# employment
class HireFor(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    # Employment
    employment_type = models.CharField(
        max_length=1, choices=EMPLOYMENT_CHOICES, null=True, blank=True)
    skill = models.ManyToManyField(
        KeySkill, related_name="%(app_label)s_%(class)s_skill")
    designation = models.ForeignKey(
        Designation, related_name="%(app_label)s_%(class)s_designation", on_delete=models.CASCADE)
    # CareerProfile
    desired_Job_type = models.CharField(
        max_length=1, choices=DESIRED_JOB_CHOICES, null=True, blank=True)
    preferred_shift = models.CharField(
        max_length=1, choices=PREFERRED_SHIFT_CHOICES, null=True, blank=True)
    functional_area = models.ForeignKey(
        FunctionalArea, related_name="%(app_label)s_%(class)s_functional_area", on_delete=models.CASCADE)
    role = models.ForeignKey(
        Role, related_name="%(app_label)s_%(class)s_role", on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.profile.user.email
