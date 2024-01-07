from django.contrib import admin
from .models import Rate, Shelter, Category, Animal, Sex
# Register your models here.


class AnimalAdmin(admin.ModelAdmin):
    model = Animal
    list_display = ('name', 'breed', 'date', 'photo', 'info', 'shelter', 'category', 'sex', 'pk')


class ShelterAdmin(admin.ModelAdmin):
    model = Animal
    list_display = ('name', 'is_active', 'user', 'pk')


admin.site.register(Rate)
admin.site.register(Shelter, ShelterAdmin)
admin.site.register(Category)
admin.site.register(Animal, AnimalAdmin)
admin.site.register(Sex)

