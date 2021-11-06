# Generated by Django 3.2 on 2021-06-05 04:25

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('primary_data', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=200)),
                ('gender', models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=1, null=True)),
                ('birth_date', models.DateField(blank=True, null=True, verbose_name='Date of Birth')),
                ('contact_number', models.CharField(blank=True, max_length=10, null=True)),
                ('contact_verified', models.BooleanField(default=False)),
                ('profile_pic', models.FileField(blank=True, null=True, upload_to='profile/')),
                ('address_proof', models.FileField(blank=True, null=True, upload_to='address/')),
                ('address_verified', models.BooleanField(default=False)),
                ('aadhar_number', models.PositiveBigIntegerField(blank=True, null=True, unique=True, validators=[django.core.validators.MaxValueValidator(999999999999)])),
                ('aadhar_verified', models.BooleanField(default=False)),
                ('pan_number', models.CharField(blank=True, max_length=10, null=True, unique=True)),
                ('pan_verified', models.BooleanField(default=False)),
                ('linked_in_profile', models.URLField(blank=True, null=True)),
                ('twitter_profile', models.URLField(blank=True, null=True)),
                ('youtube_profile', models.URLField(blank=True, null=True)),
                ('facebook_profile', models.URLField(blank=True, null=True)),
                ('instagram_profile', models.URLField(blank=True, null=True)),
                ('webpage_link', models.URLField(blank=True, null=True)),
                ('other_link', models.URLField(blank=True, null=True)),
                ('complete_profile_percentage', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(999)])),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('address', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='employer_profile_address', to='primary_data.address')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='employer_profile_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='HireFor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employment_type', models.CharField(blank=True, choices=[('F', 'Full Time'), ('P', 'Part Time')], max_length=1, null=True)),
                ('desired_Job_type', models.CharField(blank=True, choices=[('P', 'Permanent'), ('C', 'Contractual')], max_length=1, null=True)),
                ('preferred_shift', models.CharField(blank=True, choices=[('D', 'Day'), ('N', 'Night'), ('F', 'Flexible')], max_length=1, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('designation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employer_hirefor_designation', to='primary_data.designation')),
                ('functional_area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employer_hirefor_functional_area', to='primary_data.functionalarea')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employer.profile')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employer_hirefor_role', to='primary_data.role')),
                ('skill', models.ManyToManyField(related_name='employer_hirefor_skill', to='primary_data.KeySkill')),
            ],
        ),
    ]