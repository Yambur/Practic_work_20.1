from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView, DetailView
from pytils.translit import slugify

from dogs.forms import DogForm, ParentForm
from dogs.models import Breed, Dog, Parent


class IndexView(TemplateView):
    template_name = 'dogs/index.html'
    extra_context = {
        'title': 'Питомник - Главная'
    }

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['object_list'] = Breed.objects.all()[:3]
        return context_data


class BreedListView(ListView):
    model = Breed
    extra_context = {
        'title': 'Питомник - Все наши породы'
    }


class BreedDetailView(DetailView):
    model = Breed
    success_url = reverse_lazy('dogs:breeds')



class DogListView(ListView):
    model = Dog

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(breed_id=self.kwargs.get('pk'))
        return queryset

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)

        breed_item = Breed.objects.get(pk=self.kwargs.get('pk'))
        context_data['breed_pk'] = 'breed_item.pk',
        context_data['title'] = f'Собаки породы - Все наши породы {breed_item.name}'

        return context_data




class DogCreateView(CreateView):
    model = Dog
    form_class = DogForm
    success_url = reverse_lazy('dogs:breeds')

    def form_valid(self, form):
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()
        return super().form_valid(form)


class DogUpdateView(UpdateView):
    model = Dog
    form_class = DogForm

    # success_url = reverse_lazy('dogs:breeds')

    def get_success_url(self):
        return reverse('dogs:dogs_update', args=[self.kwargs.get('pk')])

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        ParentFormset = inlineformset_factory(Dog, Parent, form=ParentForm, extra=1)
        if self.request.method == 'POST':
            formset = ParentFormset(self.request.POST, instance=self.object)
        else:
            formset = ParentFormset(instance=self.object)

        context_data['formset'] = formset
        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']
        self.object = form.save()

        if formset.is_valid():
            formset.instance = self.object
            formset.save()
        return super().form_valid(form)


class DogDetailView(DetailView):
    model = Dog




class DogDeleteView(DeleteView):
    model = Dog
    success_url = reverse_lazy('dog:breeds')


"""def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        breed = request.POST.get('breed')
        photo = request.POST.get('foto')
        birth_day = request.POST.get('dr')
        print(f'{name} {breed} {photo} {birth_day}')
    return render(request, 'dogs/base.html')"""
