# Generated by Django 3.2.16 on 2022-10-12 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='fireDate',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Дата увольнения'),
        ),
    ]