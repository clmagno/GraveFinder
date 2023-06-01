# Generated by Django 4.2.1 on 2023-05-30 12:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0004_reservation_block_no_reservation_lot_no"),
    ]

    operations = [
        migrations.RenameField(
            model_name="lot",
            old_name="lat1",
            new_name="lat_long1",
        ),
        migrations.RenameField(
            model_name="lot",
            old_name="lat2",
            new_name="lat_long2",
        ),
        migrations.RenameField(
            model_name="lot",
            old_name="lat3",
            new_name="lat_long3",
        ),
        migrations.RenameField(
            model_name="lot",
            old_name="lat4",
            new_name="lat_long4",
        ),
        migrations.RemoveField(
            model_name="lot",
            name="long1",
        ),
        migrations.RemoveField(
            model_name="lot",
            name="long2",
        ),
        migrations.RemoveField(
            model_name="lot",
            name="long3",
        ),
        migrations.RemoveField(
            model_name="lot",
            name="long4",
        ),
    ]