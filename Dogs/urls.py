
from django.urls import path

from Dogs.views import index

urlpatterns = [
    path('', index)
]