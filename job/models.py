import datetime
from django.db import models
from django.core.validators import MaxValueValidator
from primary_data.models import *
from employer.models import Profile as EmployerProfile
from jobseeker.models import Profile as JobSeekerProfile
from app.choices import *

# Create your models here.


class Job(models.Model):
    employer = models.ForeignKey(EmployerProfile, on_delete=models.CASCADE,)
    job_title = models.CharField(max_length=200)
    job_description = models.TextField(null=True, blank=True)
    job_status = models.CharField(
        max_length=2, choices=JOB_STATUS, default='D')
    employment_type = models.CharField(
        max_length=1, choices=EMPLOYMENT_CHOICES, null=True, blank=True)
    job_shift = models.CharField(
        max_length=1, choices=PREFERRED_SHIFT_CHOICES, null=True, blank=True)
    min_experience = models.PositiveIntegerField(
        validators=[MaxValueValidator(99)], blank=True, null=True)
    max_experience = models.PositiveIntegerField(
        validators=[MaxValueValidator(99)], blank=True, null=True)
    min_age = models.PositiveIntegerField(
        validators=[MaxValueValidator(99)], blank=True, null=True)
    max_age = models.PositiveIntegerField(
        validators=[MaxValueValidator(99)], blank=True, null=True)
    min_ctc = models.PositiveIntegerField(
        validators=[MaxValueValidator(9999999)], blank=True, null=True)
    max_ctc = models.PositiveIntegerField(
        validators=[MaxValueValidator(9999999)], blank=True, null=True)
    preferred_gender = models.CharField(
        max_length=1, choices=GENDER_CHOICES, null=True, blank=True)
    designation = models.ForeignKey(Designation, on_delete=models.CASCADE)
    functional_area = models.ForeignKey(
        FunctionalArea, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    skill = models.ManyToManyField(KeySkill)
    jobseeker = models.ManyToManyField(JobSeekerProfile)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)


class Education(models.Model):
    job = models.ForeignKey(
        Job, on_delete=models.CASCADE, null=True, blank=True)
    jobseeker = models.ForeignKey(
        JobSeekerProfile, on_delete=models.CASCADE, null=True, blank=True)
    education_type = models.CharField(
        max_length=2, choices=EDUCATION_CHOICES, null=True, blank=True)
    course_name = models.ForeignKey(
        Course, related_name="%(app_label)s_%(class)s_course_name",
        null=True, blank=True, on_delete=models.CASCADE)
    passing_out_year = models.IntegerField(
        choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    university = models.ForeignKey(
        University, related_name="%(app_label)s_%(class)s_university",
        null=True, blank=True,  on_delete=models.CASCADE)
    board_name = models.ForeignKey(
        Board, related_name="%(app_label)s_%(class)s_board_name", null=True, blank=True,  on_delete=models.CASCADE)
    school_medium = models.ForeignKey(
        SchoolMedium, related_name="%(app_label)s_%(class)s_school_medium",
        null=True, blank=True,  on_delete=models.CASCADE)
    specialization = models.ForeignKey(
        Specialization, related_name="%(app_label)s_%(class)s_specialization",
        null=True, blank=True, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.profile.user.email
