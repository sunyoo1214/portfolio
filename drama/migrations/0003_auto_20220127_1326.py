# Generated by Django 3.2.9 on 2022-01-27 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drama', '0002_auto_20220127_1313'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='modify_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='modify_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
