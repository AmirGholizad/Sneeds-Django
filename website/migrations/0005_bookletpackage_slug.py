# Generated by Django 2.0.5 on 2018-10-22 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_bookletpackage_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookletpackage',
            name='slug',
            field=models.SlugField(default='', unique=True),
        ),
    ]