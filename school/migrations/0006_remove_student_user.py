# Generated by Django 5.1.5 on 2025-01-29 10:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0005_alter_student_level'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='user',
        ),
    ]
