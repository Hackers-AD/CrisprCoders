# Generated by Django 3.2.14 on 2022-09-21 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='maritial_status',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]