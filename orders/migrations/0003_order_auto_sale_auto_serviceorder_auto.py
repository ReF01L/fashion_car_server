# Generated by Django 4.2.4 on 2023-09-13 09:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('automobile', '0001_initial'),
        ('orders', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='auto',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='automobile.auto', verbose_name='Автомобиль'),
        ),
        migrations.AddField(
            model_name='sale',
            name='auto',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='automobile.auto', verbose_name='Автомобиль'),
        ),
        migrations.AddField(
            model_name='serviceorder',
            name='auto',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='automobile.auto', verbose_name='Автомобиль'),
        ),
    ]