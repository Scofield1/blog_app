# Generated by Django 4.0 on 2022-03-08 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilemodel',
            name='image',
            field=models.ImageField(default='profile_pic.svg', upload_to='profile'),
        ),
    ]
