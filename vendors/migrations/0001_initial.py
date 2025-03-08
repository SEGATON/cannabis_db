# Generated by Django 4.2.18 on 2025-02-23 18:57

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('catalog', '0001_initial'),
        ('addresses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.CharField(max_length=255)),
                ('description', ckeditor.fields.RichTextField(blank=True, max_length=1000, null=True)),
                ('vendor_logo', models.ImageField(blank=True, default='', null=True, upload_to='media/VENDORS/VENDORS_LOGOS/')),
                ('vendor_cover_image', models.ImageField(blank=True, default='', null=True, upload_to='media/VENDORS/VENDORS_COVER_IMAGES/')),
                ('addresses', models.ManyToManyField(blank=True, null=True, to='addresses.address')),
                ('products', models.ManyToManyField(blank=True, null=True, to='catalog.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
