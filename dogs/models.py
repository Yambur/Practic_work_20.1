from django.db import models
from django.urls import reverse

NULLABLE = {'blank': True, 'null': True}


class Breed(models.Model):
    name = models.CharField(max_length=150, verbose_name='Порода')
    description = models.TextField(**NULLABLE)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'порода'
        verbose_name_plural = 'породы'


class Dog(models.Model):
    name = models.CharField(max_length=150, verbose_name='Кличка')
    # breed = models.CharField(max_length=150, verbose_name='Порода')
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE, verbose_name='Порода')
    photo = models.ImageField(upload_to='dogs/', **NULLABLE, verbose_name='Фото')
    birth_day = models.DateTimeField(**NULLABLE, verbose_name='Дата рождения')

    #def get_absolute_url(self):
    #    return reverse('dogs:detail', args=[str(self.id)])

    def __str__(self):
        return f'{self.name} {self.breed} {self.photo} {self.birth_day}'

    class Meta:
        verbose_name = 'собака'
        verbose_name_plural = 'собаки'

class Parent(models.Model):
    dog = models.ForeignKey(Dog, on_delete=models.CASCADE)
    name = models.CharField(max_length=150, verbose_name='Кличка')
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE, verbose_name='Порода')
    birth_day = models.DateTimeField(**NULLABLE, verbose_name='Дата рождения')

    def __str__(self):
        return f'{self.name} {self.breed}:{self.birth_day}'

    class Meta:
        verbose_name = 'предок'
        verbose_name_plural = 'предки'