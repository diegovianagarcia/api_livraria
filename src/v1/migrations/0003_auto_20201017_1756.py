# Generated by Django 2.2.5 on 2020-10-17 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('v1', '0002_auto_20201017_0007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserve',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
