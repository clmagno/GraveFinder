# Generated by Django 4.2.1 on 2023-05-30 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0002_customuser_username_alter_customuser_email_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="customuser",
            old_name="name",
            new_name="first_name",
        ),
        migrations.AddField(
            model_name="customuser",
            name="last_name",
            field=models.CharField(default="", max_length=30),
        ),
    ]
