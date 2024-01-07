from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView, LoginView


urlpatterns = [
    path('animals/', AnimalList.as_view(), name='animal_list'),
    path('category/<int:pk>', AnimalOfCategory.as_view(), name='animal_of_category'),
    path('sex/<int:pk>', AnimalOfSex.as_view(), name='animal_of_sex'),

    path('animal/<int:pk>', AnimalDetail.as_view(), name='animal_detail'),

    path('animal/create', AnimalCreate.as_view(), name='animal_create'),
    path('animal/update/<int:pk>', AnimalList.as_view(), name='animal_update'),
    path('animal/delete/<int:pk>', AnimalDelete.as_view(), name='animal_delete'),

    path('shelter-create/', ShelterCreate.as_view(), name='shelter_create'),
    path('shelter/animals/', ShelterAnimalList.as_view(), name='shelter_animals_list'),

    path('user/cabinet', UserCabinet.as_view(), name='user_cabinet'),
    path('shelter/cabinet', ShelterCabinet.as_view(), name='animal_delete'),

    path('signin/', sign_in, name='sign_in'),
    path('login/', LoginView.as_view(template_name='login.html'), name='log_in'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='log_out'),

]