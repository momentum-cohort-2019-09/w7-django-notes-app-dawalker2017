# Generated by Django 2.2.6 on 2019-10-28 02:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectNote', '0007_auto_20191028_0222'),
    ]

    operations = [
        migrations.RenameField(
            model_name='noteitem',
            old_name='checklist',
            new_name='note',
        ),
    ]
