# Generated by Django 3.0.4 on 2020-03-22 05:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='nombre',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='usuario',
            new_name='username',
        ),
    ]
