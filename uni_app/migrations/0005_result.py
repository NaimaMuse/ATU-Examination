# Generated by Django 5.1 on 2024-08-21 13:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uni_app', '0004_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marks_obtained', models.FloatField()),
                ('grade', models.CharField(max_length=2)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uni_app.course')),
                ('semester', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uni_app.semester')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uni_app.student')),
            ],
            options={
                'unique_together': {('student', 'course', 'semester')},
            },
        ),
    ]