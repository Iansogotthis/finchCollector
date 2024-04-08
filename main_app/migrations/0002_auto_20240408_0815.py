# Generated by Django 3.2.12 on 2024-04-08 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='finch',
            old_name='size',
            new_name='age',
        ),
        migrations.AddField(
            model_name='finch',
            name='habitat',
            field=models.CharField(default='forest', max_length=50),
        ),
    ]
