from django.db import models

# Create your models here.
from datetime import datetime
from django.db import models

from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser


#  модель рейтинга
class Rate(models.Model):
    rate = models.IntegerField()

    user = models.OneToOneField(User, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.rate}'

    def update_rate(self):
        self.rate += 1
        self.save()


#  модель приюта
class Shelter(AbstractBaseUser):
    email = models.EmailField(max_length=70, unique=True)
    name = models.CharField(max_length=50, blank=True, unique=True)
    city = models.CharField(max_length=50)
    year_of_foundation = models.DateField()
    phone = models.CharField(max_length=11, blank=True, unique=True)
    address = models.CharField(max_length=50, blank=True, unique=True)
    link = models.URLField(blank=True, unique=True)
    is_active = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'


#  модель категории
class Category(models.Model):
    CHOICES = [
        ('cat', 'cats'),
        ('dog', 'dogs'),
    ]
    category = models.CharField(max_length=3, choices=CHOICES)

    def __str__(self):
        return self.category


#  модель пола
class Sex(models.Model):
    CHOICES = [
        ('M', 'masculine'),
        ('F', 'feminine'),
    ]
    sex = models.CharField(max_length=10, choices=CHOICES)


#  модель питомца
class Animal(models.Model):
    date = models.DateField()
    name = models.CharField(max_length=15)
    breed = models.CharField(max_length=15)
    photo = models.ImageField(upload_to='animals/', blank=True, null=True)
    info = models.TextField()

    shelter = models.ForeignKey(Shelter, on_delete=models.PROTECT)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    sex = models.ForeignKey(Sex, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.date}, {self.name}, {self.breed}, {self.info}'

    def age(self):
        return datetime.date(datetime.today()) - self.date
