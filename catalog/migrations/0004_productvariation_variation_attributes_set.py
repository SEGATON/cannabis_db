# Generated by Django 4.2.18 on 2025-02-24 11:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_productvariation_slug_productvariation_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='productvariation',
            name='variation_attributes_set',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.attributesset'),
        ),
    ]
