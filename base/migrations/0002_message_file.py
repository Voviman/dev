# Generated by Django 4.2 on 2023-06-06 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='file',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
