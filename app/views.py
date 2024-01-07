from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView, TemplateView
from django.contrib.auth.mixins import PermissionRequiredMixin

from .models import Animal, Shelter, Category, Sex
from .forms import AnimalCreateForm, ShelterCreateForm, RegistrationForm


# список питомцев
class AnimalList(ListView):
    model = Animal
    template_name = 'animal_list.html'
    context_object_name = 'animals'
    paginate_by = 15


# питомцы по определенной категории
class AnimalOfCategory(ListView):
    model = Animal
    template_name = 'animal_of_category.html'
    context_object_name = 'animals'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.get(pk=self.kwargs['pk'])
        return context


# питомцы по полу
class AnimalOfSex(ListView):
    model = Animal
    template_name = 'animal_of_sex.html'
    context_object_name = 'animals'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sex'] = Sex.objects.get(pk=self.kwargs['pk'])
        return context

    def get_queryset(self):
        return Animal.objects.filter(sex=self.kwargs['pk'])


# представление одного питомца
class AnimalDetail(DetailView):
    model = Animal
    template_name = 'animal_detail.html'
    context_object_name = 'animal'


# создание питомца
class AnimalCreate(PermissionRequiredMixin, CreateView):
    permission_required = 'app.add_animal'
    model = Animal
    form_class = AnimalCreateForm
    template_name = 'animal_create.html'
    success_url = reverse_lazy('')

    def form_valid(self, form):
        animal = form.save(commit=False)
        animal.shelter = Shelter.objects.get(user=self.request.user)
        return super().form_valid(form)


# изменение питомца
class AnimalUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = 'app.update_animal'
    model = Animal
    form_class = AnimalCreateForm
    template_name = 'animal_create.html'
    success_url = reverse_lazy('')

    def form_valid(self, form):
        animal = form.save(commit=False)
        animal.shelter = Shelter.objects.get(user=self.request.user)
        return super().form_valid(form)


# удаление питомца
class AnimalDelete(PermissionRequiredMixin, DeleteView):
    permission_required = 'app.add_animal'
    model = Animal
    template_name = 'animal_delete.html'
    context_object_name = 'animal'
    success_url = reverse_lazy('animal_list')

    # проверка юзера
    def get(self, *args, **kwargs):
        user = self.request.user
        animal = Animal.objects.get(pk=kwargs['pk'])
        if animal.shelter.user != user:
            return redirect('animal_list')
        resp = super().get(*args, **kwargs)
        return resp


# представление кабинета приюта
class ShelterCabinet(TemplateView):
    template_name = 'shelter_cabinet.html'


# создание приюта
class ShelterCreate(PermissionRequiredMixin, CreateView):
    permission_required = 'app.add_shelter'
    model = Shelter
    form_class = ShelterCreateForm
    template_name = 'shelter_create.html'
    success_url = reverse_lazy('animal_create')

    def form_valid(self, form):
        shelter = form.save(commit=False)
        shelter.user = self.request.user
        return super().form_valid(form)


# список питомцев приюта
class ShelterAnimalList(PermissionRequiredMixin, ListView):
    permission_required = 'app.add_shelter'
    model = Animal
    template_name = 'shelter_animals_list.html'
    context_object_name = 'animals'
    paginate_by = 15

    # ToDo: check
    def get_queryset(self):
        queryset = super().get_queryset()
        shelter = Shelter.objects.get(user=self.request.user)
        return queryset.filter(shelter=shelter)


# представление кабинета пользователя
class UserCabinet(TemplateView):
    template_name = 'user_cabinet.html'


# регистрация для простых пользователей
def sign_in(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('animal_list')

    else:
        form = RegistrationForm()
    return render(request, 'user_registration.html', context={'form': form})





