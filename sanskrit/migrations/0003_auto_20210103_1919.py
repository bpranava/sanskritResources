# Generated by Django 3.1.4 on 2021-01-03 13:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sanskrit', '0002_auto_20210103_1854'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Chapters',
            new_name='Chapter',
        ),
        migrations.RenameModel(
            old_name='Contents',
            new_name='Content',
        ),
        migrations.RenameModel(
            old_name='Resources',
            new_name='Resource',
        ),
    ]