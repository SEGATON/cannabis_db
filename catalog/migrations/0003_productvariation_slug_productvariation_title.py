# Generated by Django 4.2.18 on 2025-02-24 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_rename_productvariationset_productvariationsset_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='productvariation',
            name='slug',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='productvariation',
            name='title',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
