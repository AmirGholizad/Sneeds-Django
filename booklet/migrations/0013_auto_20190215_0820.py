# Generated by Django 2.1.3 on 2019-02-15 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booklet', '0012_auto_20190215_0817'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booklet',
            name='tags',
            field=models.ManyToManyField(blank=True, help_text="Don't change this if you are creating new booklet. Only change this if it is necessary.", null=True, to='booklet.Tag'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='slug',
            field=models.SlugField(help_text='If you are adding this tag for first time, leave this field blank.Only change this field if there is a mistake or for other purposes ...', max_length=2000, unique=True),
        ),
    ]
