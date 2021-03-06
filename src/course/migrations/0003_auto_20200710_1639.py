# Generated by Django 3.0.4 on 2020-07-10 16:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_auto_20200612_1341'),
        ('employee', '0005_auto_20200613_0919'),
        ('course', '0002_auto_20200612_1341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='employee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='employee.Employee'),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='student',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='student.Student'),
        ),
    ]
