# Generated by Django 3.1.4 on 2021-01-03 13:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sanskrit', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chapters',
            old_name='name',
            new_name='chapterName',
        ),
        migrations.RenameField(
            model_name='resources',
            old_name='resouceName',
            new_name='resourceName',
        ),
    ]
