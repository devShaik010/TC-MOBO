# Generated by Django 4.2.5 on 2023-09-29 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ink_Spot', '0017_book_location'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='desc',
            new_name='about',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='name',
            new_name='model',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='owner',
            new_name='owner_name',
        ),
        migrations.AddField(
            model_name='book',
            name='contact',
            field=models.CharField(default='null', max_length=15),
        ),
    ]
