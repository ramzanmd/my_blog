# Generated by Django 4.1.3 on 2022-11-17 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_post_detail'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='my_images'),
        ),
    ]
