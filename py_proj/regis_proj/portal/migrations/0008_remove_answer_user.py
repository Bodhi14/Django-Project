# Generated by Django 4.1.5 on 2023-01-30 23:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0007_alter_answer_ans1_alter_answer_ans2_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='user',
        ),
    ]
