# Generated by Django 3.2 on 2021-06-05 04:25

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('jobseeker', '0001_initial'),
        ('employer', '0001_initial'),
        ('primary_data', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(max_length=200)),
                ('job_description', models.TextField(blank=True, null=True)),
                ('job_status', models.CharField(choices=[('D', 'DRAFT'), ('P', 'PUBLISHED'), ('E', 'EXPIRED'), ('DE', 'DELETED')], default='D', max_length=2)),
                ('employment_type', models.CharField(blank=True, choices=[('F', 'Full Time'), ('P', 'Part Time')], max_length=1, null=True)),
                ('job_shift', models.CharField(blank=True, choices=[('D', 'Day'), ('N', 'Night'), ('F', 'Flexible')], max_length=1, null=True)),
                ('min_experience', models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(99)])),
                ('max_experience', models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(99)])),
                ('min_age', models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(99)])),
                ('max_age', models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(99)])),
                ('min_ctc', models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(9999999)])),
                ('max_ctc', models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(9999999)])),
                ('preferred_gender', models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=1, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('address', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='primary_data.address')),
                ('designation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='primary_data.designation')),
                ('employer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employer.profile')),
                ('functional_area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='primary_data.functionalarea')),
                ('jobseeker', models.ManyToManyField(to='jobseeker.Profile')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='primary_data.role')),
                ('skill', models.ManyToManyField(to='primary_data.KeySkill')),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('education_type', models.CharField(blank=True, choices=[('10', '10th'), ('12', '12th'), ('GD', 'Graduation/Diploma'), ('MP', 'Masters/Post-Graduation'), ('DP', 'Doctorate/PhD')], max_length=2, null=True)),
                ('passing_out_year', models.IntegerField(choices=[(1970, 1970), (1971, 1971), (1972, 1972), (1973, 1973), (1974, 1974), (1975, 1975), (1976, 1976), (1977, 1977), (1978, 1978), (1979, 1979), (1980, 1980), (1981, 1981), (1982, 1982), (1983, 1983), (1984, 1984), (1985, 1985), (1986, 1986), (1987, 1987), (1988, 1988), (1989, 1989), (1990, 1990), (1991, 1991), (1992, 1992), (1993, 1993), (1994, 1994), (1995, 1995), (1996, 1996), (1997, 1997), (1998, 1998), (1999, 1999), (2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020), (2021, 2021)], default=2021)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('board_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='job_education_board_name', to='primary_data.board')),
                ('course_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='job_education_course_name', to='primary_data.course')),
                ('job', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='job.job')),
                ('jobseeker', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='jobseeker.profile')),
                ('school_medium', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='job_education_school_medium', to='primary_data.schoolmedium')),
                ('specialization', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='job_education_specialization', to='primary_data.specialization')),
                ('university', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='job_education_university', to='primary_data.university')),
            ],
        ),
    ]
