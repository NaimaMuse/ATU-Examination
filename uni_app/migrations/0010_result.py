# Generated by Django 5.0.4 on 2024-08-23 18:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uni_app', '0009_delete_transcript'),
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.DecimalField(decimal_places=2, max_digits=5)),
                ('grade', models.CharField(blank=True, max_length=2, null=True)),
                ('sgpa', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True)),
                ('ogpa', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uni_app.course')),
                ('semester', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uni_app.semester')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uni_app.student')),
            ],
        ),
    ]
