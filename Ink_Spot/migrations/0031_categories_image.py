# Generated by Django 4.2.5 on 2023-10-12 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ink_Spot', '0030_rename_status_order_dispatch'),
    ]

    operations = [
        migrations.AddField(
            model_name='categories',
            name='image',
            field=models.ImageField(default='exit', upload_to='Uploads/product'),
            preserve_default=False,
        ),
    ]
