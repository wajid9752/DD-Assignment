# Generated by Django 5.0 on 2024-01-01 11:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0004_alter_task_assigned_to_alter_task_project'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='members',
        ),
    ]
