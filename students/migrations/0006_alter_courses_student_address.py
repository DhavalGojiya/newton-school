# Generated by Django 4.1.2 on 2022-12-19 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0005_courses_student_address_courses_student_city_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='student_address',
            field=models.TextField(),
        ),
    ]