# Generated by Django 3.1.3 on 2020-12-09 18:47

from django.db import migrations


class Migration(migrations.Migration):
    atomic = False
    dependencies = [
        ('core', '0007_course'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Course',
            new_name='CourseOld',
        ),
        migrations.AlterModelOptions(
            name='courseold',
            options={'verbose_name': 'curso', 'verbose_name_plural': 'cursos'},
        ),
    ]
