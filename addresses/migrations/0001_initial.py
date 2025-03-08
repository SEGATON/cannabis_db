# Generated by Django 4.2.18 on 2025-02-23 18:57

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields
import localflavor.us.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address_type', models.CharField(blank=True, choices=[('billing_address', 'Billing Address'), ('shipping_address', 'Shipping Address'), ('p_o_box', 'P.O Box')], max_length=255, null=True)),
                ('address_street_name_line_1', models.CharField(blank=True, max_length=255, null=True)),
                ('address_street_name_line_2', models.CharField(blank=True, max_length=255, null=True)),
                ('address_city', models.CharField(blank=True, max_length=255, null=True)),
                ('address_state', localflavor.us.models.USStateField(max_length=2)),
                ('address_zip_code', localflavor.us.models.USZipCodeField(max_length=10)),
                ('address_country', django_countries.fields.CountryField(max_length=2)),
                ('notes', ckeditor.fields.RichTextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
