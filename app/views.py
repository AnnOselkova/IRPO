from django.contrib.auth import login, authenticate
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView, TemplateView
from .models import Animal, Shelter
from .forms import AnimalCreateForm, ShelterLoginForm


#  список питомцев
class AnimalList(ListView):
    model = Animal
    template_name = ''
    context_object_name = 'animals'
    paginate_by = 15


#  представление одного питомца
class AnimalDetail(DetailView):
    model = Animal
    template_name = ''
    context_object_name = 'animal'


#  создание питомца
class AnimalCreate(CreateView):
    model = Animal
    form_class = AnimalCreateForm
    template_name = 'animal_create.html'
    success_url = reverse_lazy('')

    def form_valid(self, form):
        animal = form.save(commit=False)
        print(111111111111, self.request.user)
        animal.shelter = self.request.shelter
        return super().form_valid(form)


#  удаление питомца
class AnimalDelete(DeleteView):
    model = Animal
    template_name = ''
    context_object_name = 'animal'
    success_url = reverse_lazy('')


#  представление кабинета пользователя
class UserCabinet(TemplateView):
    template_name = ''


#  представление кабинета приюта
class ShelterCabinet(TemplateView):
    template_name = ''


class ShelterAnimalList(ListView):
    model = Animal
    template_name = ''
    context_object_name = 'animals'
    paginate_by = 15

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     # ToDo: check request.shelter
    #     return queryset.filter(shelter=self.request.shelter)


def shelter_login(request):
    if request.method == 'POST':
        form = ShelterLoginForm(data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            try:
                shelter = authenticate(Shelter.objects.get(email=email, password=password))
            except:
                shelter = authenticate(email=email, password=password)
            if shelter is not None:
                login(request, shelter)
                return HttpResponse('Error1111111')
            else:
                return HttpResponse('Error2222222')
        else:
            return HttpResponse('Error3333333')
    form = ShelterLoginForm()
    return render(request, 'shelter_login.html', {'form': form})



