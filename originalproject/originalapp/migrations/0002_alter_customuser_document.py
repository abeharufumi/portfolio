# Generated by Django 3.2 on 2023-02-06 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('originalapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='document',
            field=models.ImageField(null=True, upload_to='document/'),
        ),
    ]
