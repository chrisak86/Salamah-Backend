# Generated by Django 4.2.16 on 2024-09-19 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0019_ticket_created_at_ticket_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]