from django.urls import path

from dogs.apps import DogsConfig
from dogs.views import IndexView, DogListView, DogCreateView, DogUpdateView, DogDeleteView, \
    BreedDetailView, BreedListView, DogDetailView

app_name = DogsConfig.name

urlpatterns = [
    path('', IndexView.as_view(), name='index'),

    path('breeds/', BreedListView.as_view(), name='breeds'),
    path('breed/detail/<int:pk>', BreedDetailView.as_view(), name='breed_detail'),

    path('<int:pk>/dogs/', DogListView.as_view(), name='breeds_dogs'),
    path('dogs/create/', DogCreateView.as_view(), name='dog_create'),
    path('dogs/<int:pk>/update/', DogUpdateView.as_view(), name='dogs_update'),
    path('dogs/<int:pk>/detail/', DogDetailView.as_view(), name='dogs_detail'),
    path('dogs/delete/<int:pk>', DogDeleteView.as_view(), name='dogs_delete'),

]
