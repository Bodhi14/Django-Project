# Generated by Django 4.1.5 on 2023-01-29 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Responses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ans1', models.TextField(max_length=300)),
                ('ans2', models.TextField(max_length=300)),
                ('ans3', models.TextField(max_length=300)),
                ('ans4', models.TextField(max_length=300)),
            ],
        ),
    ]
