# Generated by Django 4.1.7 on 2023-04-10 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("finances", "0003_finance_amount"),
    ]

    operations = [
        migrations.AddField(
            model_name="finance",
            name="date_time",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
