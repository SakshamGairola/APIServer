# Generated by Django 4.1.1 on 2022-09-27 14:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('APIServer', '0002_rename_bank_branches_bank_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='branches',
            old_name='bank_id',
            new_name='bank',
        ),
    ]
