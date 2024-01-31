from django.shortcuts import render

from dogs.models import Breed, Dog


def index(request):
    context = {
        'object_list': Breed.objects.all()[:3],
        'title': 'Питомник - Главная'
    }
    return render(request, 'dogs/index.html', context)


def breeds(request):
    context = {
        'object_list': Breed.objects.all(),
        'title': 'Питомник - Все наши породы'
    }
    return render(request, 'dogs/breeds.html', context)


def breeds_dogs(request, pk):
    breed_item = Breed.objects.get(pk=pk)
    context = {
        'object_list': Dog.objects.filter(breed_id=pk),
        'title': f'Собаки породы - Все наши породы {breed_item.name}'
    }
    return render(request, 'dogs/dogs.html', context)



"""def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        breed = request.POST.get('breed')
        photo = request.POST.get('foto')
        birth_day = request.POST.get('dr')
        print(f'{name} {breed} {photo} {birth_day}')
    return render(request, 'dogs/base.html')"""
