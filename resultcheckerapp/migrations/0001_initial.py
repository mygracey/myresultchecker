# Generated by Django 3.2.25 on 2024-06-18 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ResultModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studentname', models.CharField(max_length=300, null=True)),
                ('email', models.CharField(max_length=300, null=True)),
                ('studentID', models.CharField(max_length=10, null=True)),
                ('math', models.CharField(max_length=10, null=True)),
                ('english', models.CharField(max_length=10, null=True)),
                ('science', models.CharField(max_length=10, null=True)),
            ],
        ),
    ]
