# Generated by Django 4.2.3 on 2023-08-28 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rental',
            name='return_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
