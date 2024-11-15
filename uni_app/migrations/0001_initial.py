# Generated by Django 5.1 on 2024-08-20 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('department', models.CharField(max_length=100)),
                ('faculty_id', models.CharField(max_length=20, unique=True)),
                ('course_taught', models.CharField(max_length=100)),
            ],
        ),
    ]
