# Generated by Django 2.2.5 on 2020-10-17 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('v1', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ['title']},
        ),
        migrations.AlterModelOptions(
            name='client',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='interest',
            options={'ordering': ['days']},
        ),
        migrations.AlterModelOptions(
            name='reserve',
            options={'ordering': ['client']},
        ),
        migrations.AlterField(
            model_name='reserve',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
