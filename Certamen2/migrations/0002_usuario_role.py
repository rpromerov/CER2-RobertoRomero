# Generated by Django 4.2.13 on 2024-06-01 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Certamen2', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='role',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]
