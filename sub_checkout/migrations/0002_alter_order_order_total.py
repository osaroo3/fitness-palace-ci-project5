# Generated by Django 3.2.25 on 2024-06-29 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sub_checkout', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_total',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
