# Generated by Django 4.2.2 on 2025-04-15 01:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cannabis_db', '0004_brand_brand_strains_alter_brand_brand_address_and_more'),
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='brands',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cannabis_db.brand'),
        ),
        migrations.DeleteModel(
            name='Brand',
        ),
    ]
