# Generated by Django 2.0.3 on 2018-10-29 03:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0007_auto_20181029_0908'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tag',
            old_name='Tag_description',
            new_name='description',
        ),
    ]