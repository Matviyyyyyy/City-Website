# Generated by Django 5.1.2 on 2024-12-16 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_new_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='new',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='news_images/'),
        ),
    ]
