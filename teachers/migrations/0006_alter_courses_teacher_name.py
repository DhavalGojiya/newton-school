# Generated by Django 4.1.2 on 2022-12-16 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0005_courses_teacher_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='teacher_name',
            field=models.CharField(max_length=120),
        ),
    ]