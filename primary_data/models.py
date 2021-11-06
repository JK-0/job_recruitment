from django.db import models
from django.core.validators import MaxValueValidator
from app.choices import EDUCATION_CHOICES

# Create your models here.


class Country(models.Model):
    name = models.CharField(max_length=200)
    iso2 = models.CharField(max_length=50, blank=True)
    iso3 = models.CharField(max_length=50, blank=True)
    phone_code = models.CharField(blank=True, max_length=100)
    capital = models.CharField(max_length=100, blank=True)
    currency = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class State(models.Model):
    name = models.CharField(max_length=200)
    country = models.ForeignKey(Country, on_delete=models.RESTRICT)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=200)
    country = models.ForeignKey(Country, on_delete=models.RESTRICT)
    state = models.ForeignKey(State, on_delete=models.RESTRICT)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


# education
class University(models.Model):
    name = models.CharField(max_length=200)
    country = models.ForeignKey(Country, on_delete=models.RESTRICT)
    domain = models.CharField(max_length=200, blank=True)
    web_page = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


# education
class Board(models.Model):
    board_name = models.CharField(max_length=200, unique=True)
    board_type = models.CharField(max_length=200)
    verified = models.BooleanField(default=False)

    def __str__(self):
        return self.board_name


# education
class SchoolMedium(models.Model):
    school_medium = models.CharField(max_length=200, unique=True)
    verified = models.BooleanField(default=False)

    def __str__(self):
        return self.school_medium


# education
class Course(models.Model):
    course_name = models.CharField(max_length=200)
    education_type = models.CharField(
        max_length=2,
        choices=EDUCATION_CHOICES
    )
    verified = models.BooleanField(default=False)

    def __str__(self):
        return self.course_name


# education
class Specialization(models.Model):
    specialization = models.CharField(max_length=200)
    course_name = models.ForeignKey(Course, on_delete=models.RESTRICT)
    education_type = models.CharField(
        max_length=2,
        choices=EDUCATION_CHOICES
    )
    verified = models.BooleanField(default=False)

    def __str__(self):
        return self.specialization


# career profile
class Language(models.Model):
    language = models.CharField(max_length=100)
    alpha2 = models.CharField(max_length=2)
    alpha3_b = models.CharField(max_length=3)
    verified = models.BooleanField(default=False)

    def __str__(self):
        return self.language


# career profile
class FunctionalArea(models.Model):
    functional_area_name = models.CharField(max_length=100)
    verified = models.BooleanField(default=False)

    def __str__(self):
        return self.functional_area_name


# career profile
class Role(models.Model):
    role_name = models.CharField(max_length=100)
    role_group = models.CharField(max_length=100, blank=True)
    functional_area = models.ForeignKey(
        FunctionalArea, on_delete=models.RESTRICT)
    verified = models.BooleanField(default=False)

    def __str__(self):
        return self.role_name


# career profile
class PreferredLocation(models.Model):
    location = models.CharField(max_length=100, unique=True)
    verified = models.BooleanField(default=False)

    def __str__(self):
        return self.location


# in employment
class Designation(models.Model):
    designation = models.CharField(max_length=100, unique=True)
    verified = models.BooleanField(default=False)

    def __str__(self):
        return self.designation


# in employment
class KeySkill(models.Model):
    skill = models.CharField(max_length=100, unique=True)
    verified = models.BooleanField(default=False)

    def __str__(self):
        return self.skill


class Address(models.Model):
    address_one = models.CharField(max_length=100, null=True, blank=True)
    address_two = models.CharField(max_length=100, blank=True, null=True)
    address_three = models.CharField(max_length=100, blank=True, null=True)
    pin_code = models.PositiveIntegerField(
        validators=[MaxValueValidator(999999)], blank=True, null=True)
    country = models.ForeignKey(
        Country, on_delete=models.CASCADE, blank=True, null=True)
    state = models.ForeignKey(
        State, on_delete=models.CASCADE, blank=True, null=True)
    city = models.ForeignKey(
        City, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f'{self.address_one} , {self.address_two} , {self.address_three} , {self.city} , \
            {self.state} , {self.country} , {self.pin_code}'
