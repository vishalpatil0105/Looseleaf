# Generated by Django 4.0.3 on 2022-03-10 17:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SchoolAdminPortal', '0002_alter_courses_student_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='student_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='SchoolAdminPortal.students'),
        ),
    ]
