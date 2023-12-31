# Generated by Django 4.2.4 on 2023-09-19 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mulct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(verbose_name='Описание')),
                ('value', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Значение')),
            ],
        ),
        migrations.AddField(
            model_name='manager',
            name='mulcts',
            field=models.ManyToManyField(related_name='manager_mulcts', to='users.mulct', verbose_name='Штрафы'),
        ),
        migrations.AddField(
            model_name='master',
            name='mulcts',
            field=models.ManyToManyField(related_name='master_mulcts', to='users.mulct', verbose_name='Штрафы'),
        ),
    ]
