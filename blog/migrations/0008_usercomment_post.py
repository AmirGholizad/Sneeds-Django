# Generated by Django 2.1.3 on 2019-02-04 06:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_usercomment'),
    ]

    operations = [
        migrations.AddField(
            model_name='usercomment',
            name='post',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='commnets', to='blog.Post'),
        ),
    ]
