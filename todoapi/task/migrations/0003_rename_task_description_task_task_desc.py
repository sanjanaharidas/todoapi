# Generated by Django 5.0.2 on 2024-03-11 05:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0002_alter_task_date_added'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='task_description',
            new_name='task_desc',
        ),
    ]
