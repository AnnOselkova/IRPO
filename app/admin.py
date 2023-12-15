from django.contrib import admin
from .models import Rate, Shelter, Category, Animal, Sex
# Register your models here.


class AnimalAdmin(admin.ModelAdmin):
    model = Animal
    list_display = ('name', 'breed', 'date', 'photo', 'info', 'shelter', 'category', 'sex', 'pk')


admin.site.register(Rate)
admin.site.register(Shelter)
admin.site.register(Category)
admin.site.register(Animal, AnimalAdmin)
admin.site.register(Sex)

