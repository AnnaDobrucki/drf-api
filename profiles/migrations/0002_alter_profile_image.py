# Generated by Django 3.2.23 on 2024-01-22 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='../chair-and-coffee-table', upload_to='images/'),
        ),
    ]
