# Generated by Django 4.2.1 on 2023-05-30 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="customuser",
            name="username",
            field=models.CharField(default="", max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name="customuser",
            name="email",
            field=models.EmailField(default="", max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name="customuser",
            name="name",
            field=models.CharField(default="", max_length=30),
        ),
    ]