# Generated by Django 3.0.6 on 2020-05-30 14:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0003_instrumentals'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Instrumentals',
            new_name='Instrumental',
        ),
    ]