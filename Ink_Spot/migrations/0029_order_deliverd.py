# Generated by Django 4.2.5 on 2023-10-09 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ink_Spot', '0028_product_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='deliverd',
            field=models.BooleanField(default=False),
        ),
    ]
