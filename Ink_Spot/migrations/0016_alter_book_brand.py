# Generated by Django 4.2.5 on 2023-09-29 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ink_Spot', '0015_rename_a_uth_book_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='brand',
            field=models.CharField(max_length=20),
        ),
    ]
