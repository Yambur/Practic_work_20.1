from django.shortcuts import render


# Create your views here.
def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        breed = request.POST.get('breed')
        photo = request.POST.get('foto')
        birth_day = request.POST.get('dr')
        print(f'{name} {breed} {photo} {birth_day}')
    return render(request, 'dogs/index.html')
