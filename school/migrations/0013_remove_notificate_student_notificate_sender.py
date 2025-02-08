# Generated by Django 5.1.5 on 2025-02-06 06:50

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0012_notificate_read_message'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notificate',
            name='student',
        ),
        migrations.AddField(
            model_name='notificate',
            name='sender',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='sent_notification', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
