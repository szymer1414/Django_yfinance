# Generated by Django 5.1.3 on 2024-12-02 01:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0004_currencypair_base_currency_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exchangerate',
            name='currency_pair',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='currency.currencypair'),
        ),
    ]