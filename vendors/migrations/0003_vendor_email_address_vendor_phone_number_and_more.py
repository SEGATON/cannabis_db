# Generated by Django 4.2.2 on 2025-05-06 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendors', '0002_vendor_categories'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendor',
            name='email_address',
            field=models.EmailField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='vendor',
            name='phone_number',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='vendor',
            name='websiteURL',
            field=models.URLField(blank=True, max_length=300, null=True),
        ),
    ]
