# Generated by Django 3.1.4 on 2020-12-05 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='comments',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='rent',
            name='comments',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='room',
            name='comments',
            field=models.TextField(blank=True),
        ),
    ]
