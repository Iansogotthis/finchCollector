# Generated by Django 3.2.12 on 2024-04-08 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_feeding'),
    ]

    operations = [
        migrations.AddField(
            model_name='finch',
            name='last_fed_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='feeding',
            name='date',
            field=models.DateField(verbose_name='Feeding Date'),
        ),
    ]
