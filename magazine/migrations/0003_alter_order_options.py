# Generated by Django 5.0 on 2023-12-15 13:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('magazine', '0002_alter_supply_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ['date_create'], 'verbose_name': 'Заказ', 'verbose_name_plural': 'Заказы'},
        ),
    ]
