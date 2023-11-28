from django.db import models

# Create your models here.
from datetime import datetime
from django.db import models

from django.contrib.auth.models import User


class Rate(models.Model):
    rate = models.IntegerField()

    user = models.OneToOneField(User, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.rate}'

    def update_rate(self):
        self.rate += 1
        self.save()


class Shelter(models.Model):
    name = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    year_of_foundation = models.DateField()
    mail = models.EmailField(max_length=70, blank=True, unique=True)
    phone = models.CharField(max_length=11)
    address = models.CharField(max_length=50)
    link = models.URLField()

    user = models.OneToOneField(User, on_delete=models.PROTECT)


class Category(models.Model):
    CHOICES = [
        ('cat', 'cats'),
        ('dog', 'dogs'),
    ]
    category = models.CharField(max_length=3, choices=CHOICES)

    def __str__(self):
        return self.category


class Animal(models.Model):
    date = models.DateField()
    name = models.CharField(max_length=15)
    breed = models.CharField(max_length=15)
    photo = models.ImageField(upload_to='animals/', blank=True, null=True)
    info = models.TextField()

    shelter = models.ForeignKey(Shelter, on_delete=models.PROTECT)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.date}, {self.name}, {self.breed}, {self.info}'

    def age(self):
        return datetime.date(datetime.today()) - self.date
