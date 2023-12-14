from django.urls import path
from .views import *


urlpatterns = [
    path('home/', AnimalList.as_view(), name='animal_list'),
    path('create/', AnimalCreate.as_view()),
    path('login/', shelter_login)
]