import datetime

USER_CHOICES = (
    ('U', 'Undefined'),
    ('J', 'Jobseeker'),
    ('E', 'Employer'),
)

EDUCATION_CHOICES = (
    ('10', '10th'),
    ('12', '12th'),
    ('GD', 'Graduation/Diploma'),
    ('MP', 'Masters/Post-Graduation'),
    ('DP', 'Doctorate/PhD'),
)

GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Other'),
)

EMPLOYMENT_CHOICES = (
    ('F', 'Full Time'),
    ('P', 'Part Time'),
)

DESIRED_JOB_CHOICES = (
    ('P', 'Permanent'),
    ('C', 'Contractual'),
)

PREFERRED_SHIFT_CHOICES = (
    ('D', 'Day'),
    ('N', 'Night'),
    ('F', 'Flexible'),
)

MARITAL_CHOICES = (
    ('S', 'Single'),
    ('M', 'Married'),
    ('D', 'Divorced'),
)

LAC_CHOICES = [(q, str(q) + ' Lac') for q in range(1, 99)]

THOUSAND_CHOICES = [(t, str(t) + ' Thousand') for t in range(0, 100, 5)]

YEAR_CHOICES = [(y, y) for y in range(1970, datetime.date.today().year+1)]

STATUS_CHOICES = (
    ('I', 'In Progress'),
    ('F', 'Finished'),
)

PROFICIENCY_CHOICES = (
    ('B', 'Beginner'),
    ('P', 'Proficient'),
    ('E', 'Expert'),
)

JOB_STATUS = (
    ('D', 'DRAFT'),
    ('P', 'PUBLISHED'),
    ('E', 'EXPIRED'),
    ('DE', 'DELETED'),
)
