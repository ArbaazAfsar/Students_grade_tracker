# Generated by Django 5.1.4 on 2024-12-05 19:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grades', '0002_student_user'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='grade',
            unique_together={('student', 'subject')},
        ),
    ]
