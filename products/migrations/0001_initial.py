# Generated by Django 4.2.4 on 2023-09-13 09:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Название')),
                ('amount', models.PositiveIntegerField(default=0, verbose_name='Количество')),
                ('for_supply', models.BooleanField(verbose_name='Под поставку')),
                ('description', models.TextField(verbose_name='Описание')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Аксессуары в наличии',
            },
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purchase_price', models.DecimalField(decimal_places=2, max_digits=12, verbose_name='Закупочная цена')),
                ('sale_price', models.DecimalField(decimal_places=2, max_digits=12, verbose_name='Цена продажи')),
                ('product', models.OneToOneField(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.product')),
            ],
            options={
                'verbose_name': 'Цена',
                'verbose_name_plural': 'Цены',
            },
        ),
        migrations.CreateModel(
            name='ProductForSupply',
            fields=[
            ],
            options={
                'verbose_name': 'Под поставку',
                'verbose_name_plural': 'Аксессуары под заказ',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('products.product',),
        ),
        migrations.CreateModel(
            name='ProductTuning',
            fields=[
            ],
            options={
                'verbose_name': 'Тюнинг в наличии',
                'verbose_name_plural': 'Тюнинг в наличии',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('products.product',),
        ),
        migrations.CreateModel(
            name='ProductTuningForSupply',
            fields=[
            ],
            options={
                'verbose_name': 'Тюнинг под заказ',
                'verbose_name_plural': 'Тюнинг под заказ',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('products.product',),
        ),
    ]
