# Generated by Django 2.2 on 2021-03-15 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=500)),
                ('option1', models.CharField(max_length=100)),
                ('correctAnswer', models.CharField(max_length=100)),
            ],
        ),
    ]