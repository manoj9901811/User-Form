from django.db import models

class UserDetail(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]

    name = models.CharField(max_length=100, default='Unknown')
    age = models.PositiveIntegerField(default=0)
    dob = models.DateField(default='2000-01-01')
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default='Other')
    email = models.EmailField(default='noemail@example.com')
    address = models.TextField(default='N/A')
    occupation = models.CharField(max_length=100, default='Unemployed')
    phone_number = models.CharField(max_length=15, default='0000000000')
    photo = models.ImageField(upload_to='photos/', default='photos/default.png')  # optional default image

    def __str__(self):
        return self.name
