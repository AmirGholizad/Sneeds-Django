# Generated by Django 2.1.3 on 2019-02-08 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_post_aparat_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='youtube_link',
            field=models.URLField(blank=True, null=True),
        ),
    ]
