# Generated by Django 4.2.16 on 2024-09-19 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0020_alter_ticket_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='officer_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
