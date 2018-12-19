# Generated by Django 2.1.3 on 2018-12-19 16:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0008_auto_20181024_2216'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookletProblemReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='گذارش خرابی')),
                ('booklet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='problems', to='website.Booklet')),
            ],
        ),
    ]
