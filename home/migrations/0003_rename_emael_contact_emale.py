# Generated by Django 4.2.7 on 2023-12-14 22:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_rename_email_contact_emael'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='emael',
            new_name='emale',
        ),
    ]
