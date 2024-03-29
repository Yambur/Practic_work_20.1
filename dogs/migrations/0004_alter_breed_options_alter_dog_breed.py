# Generated by Django 4.2 on 2024-01-14 06:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dogs', '0003_rename_bredd_breed'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='breed',
            options={'verbose_name': 'собака', 'verbose_name_plural': 'собаки'},
        ),
        migrations.AlterField(
            model_name='dog',
            name='breed',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dogs.breed', verbose_name='Порода'),
        ),
    ]
