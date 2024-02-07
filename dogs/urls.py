from django.urls import path

from dogs.apps import DogsConfig
from dogs.views import IndexView, BreedListView, DogListView, DogCreateView, DogUpdateView, DogDeleteView, BreedDetailView

app_name = DogsConfig.name

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('breeds/', BreedListView.as_view(), name='breeds'),
    path('<int:pk>/dogs/', DogListView.as_view(), name='breeds_dogs'),
    path('breed/detail/<int:pk>', BreedDetailView.as_view(), name='breed_detail'),
    path('dogs/create', DogCreateView.as_view(), name='dog_create'),
    path('dogs/update/<int:pk>', DogUpdateView.as_view(), name='dogs_update'),
    path('dogs/delete/<int:pk>', DogDeleteView.as_view(), name='dogs_delete'),

]
