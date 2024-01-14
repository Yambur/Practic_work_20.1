from django.shortcuts import render


# Create your views here.
def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        breed = request.POST.get('breed')
        foto = request.POST.get('foto')
        dr = request.POST.get('dr')
        print(f'{name} {breed} {foto} {dr}')
    return render(request, 'Dogs/index.html')
