# Generated by Django 2.2 on 2020-12-08 06:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_ingredient'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('time_minutes', models.IntegerField(verbose_name='Time in minutes')),
                ('price', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Price')),
                ('link', models.CharField(blank=True, max_length=255, verbose_name='Link')),
                ('ingredients', models.ManyToManyField(to='core.Ingredient', verbose_name='Ingredients')),
                ('tags', models.ManyToManyField(to='core.Tag', verbose_name='Tags')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
    ]
