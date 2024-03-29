# Generated by Django 5.0 on 2024-01-01 10:34

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0003_team_project_alter_project_members_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='assigned_to',
            field=models.ForeignKey(limit_choices_to={'role': 'employee'}, on_delete=django.db.models.deletion.CASCADE, related_name='my_task', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='task',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='emp_task', to='manager.project'),
        ),
    ]
