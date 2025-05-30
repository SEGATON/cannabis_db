# Generated by Django 4.2.2 on 2025-05-23 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cannabis_db', '0013_alter_dispensary_shopping_options_and_more'),
        ('catalog', '0005_alter_brand_author_alter_brand_brand_address_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='brands',
        ),
        migrations.AlterField(
            model_name='product',
            name='product_type',
            field=models.CharField(blank=True, choices=[('single_product', 'Single product'), ('variable_product', 'Variable product'), ('digital_product', 'Digital product'), ('dropship_product', 'Dropship product'), ('seeds', 'Seeds')], max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='brands',
            field=models.ManyToManyField(related_name='product_brand', to='cannabis_db.brand'),
        ),
    ]
