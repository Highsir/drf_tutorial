# Generated by Django 4.1.5 on 2023-02-08 09:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="entry",
            name="mod_date",
        ),
        migrations.RemoveField(
            model_name="entry",
            name="pub_date",
        ),
    ]
