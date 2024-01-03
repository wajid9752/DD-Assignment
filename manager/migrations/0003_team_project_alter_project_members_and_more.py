# Generated by Django 5.0 on 2024-01-01 10:09

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0002_feedback_created_at_feedback_updated_at_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='project',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='teamProjects', to='manager.project'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='project',
            name='members',
            field=models.ManyToManyField(related_name='project_teams', through='manager.Team', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='ProjectMembership',
        ),
    ]
