# Generated by Django 4.2.5 on 2023-09-29 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ink_Spot', '0016_alter_book_brand'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='location',
            field=models.CharField(default='Null', max_length=150),
        ),
    ]
