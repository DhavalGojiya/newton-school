# Generated by Django 4.1.2 on 2023-01-02 10:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0020_remove_coursepurchases_course_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='coursepurchases',
            old_name='user',
            new_name='course_info',
        ),
        migrations.RemoveField(
            model_name='coursepurchases',
            name='student_zip',
        ),
    ]