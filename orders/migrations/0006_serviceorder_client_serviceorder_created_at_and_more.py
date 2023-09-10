# Generated by Django 4.2.4 on 2023-09-10 06:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_provider_options'),
        ('orders', '0005_alter_orderitem_provider'),
    ]

    operations = [
        migrations.AddField(
            model_name='serviceorder',
            name='client',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.client', verbose_name='Клиент'),
        ),
        migrations.AddField(
            model_name='serviceorder',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Создан'),
        ),
        migrations.AddField(
            model_name='serviceorder',
            name='manager',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.manager', verbose_name='Менеджер'),
        ),
        migrations.AddField(
            model_name='serviceorder',
            name='state',
            field=models.CharField(choices=[('WAIT', 'Ожидание'), ('PROGRESS', 'В процессе'), ('READY', 'Готов'), ('FINISHED', 'Выдан')], default='WAIT', max_length=32, verbose_name='Состояние'),
        ),
        migrations.AddField(
            model_name='serviceorder',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='Последнее изменение'),
        ),
    ]