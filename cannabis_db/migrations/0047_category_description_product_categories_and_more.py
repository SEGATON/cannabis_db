# Generated by Django 4.2.2 on 2024-11-08 02:39

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cannabis_db', '0046_category_slug_category_title_product_product_type_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, max_length=5000, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='categories',
            field=models.ManyToManyField(blank=True, null=True, to='cannabis_db.category'),
        ),
        migrations.AddField(
            model_name='product',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, max_length=5000, null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='rating',
            field=models.CharField(choices=[('4', '4'), ('5', '5'), ('2', '2'), ('3', '3'), ('1', '1')], max_length=5),
        ),
        migrations.AlterField(
            model_name='dispensary',
            name='accepted_payment_methods',
            field=models.CharField(choices=[('cash', 'Cash'), ('cash_debit_credit', 'Cash, Debit/Credit Cards'), ('debit_credit', 'Debit/Credit Cards')], max_length=50),
        ),
        migrations.AlterField(
            model_name='dispensary',
            name='shopping_options',
            field=models.CharField(blank=True, choices=[('pickup_delivery', 'Pickup/Delivery'), ('pickup', 'Pickup'), ('delivery', 'Delivery')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='effectreport',
            name='type_of_effects',
            field=models.CharField(choices=[('negative', 'Negative'), ('neutrial', 'Neutrial'), ('positive', 'Positive')], max_length=50),
        ),
        migrations.AlterField(
            model_name='feelingreport',
            name='type_of_feelings',
            field=models.CharField(choices=[('negative', 'Negative'), ('generic', 'Generic'), ('positive', 'Positive')], max_length=50),
        ),
        migrations.AlterField(
            model_name='rating',
            name='rating',
            field=models.CharField(choices=[('4', '4'), ('5', '5'), ('2', '2'), ('3', '3'), ('1', '1')], max_length=5),
        ),
        migrations.AlterField(
            model_name='strain',
            name='strain_type_label',
            field=models.CharField(blank=True, choices=[('sativa', 'Sativa'), ('hybrid', 'Hybrid'), ('indica', 'Indica')], max_length=70, null=True),
        ),
        migrations.AlterField(
            model_name='strainlineagedetailslistitem',
            name='strain_lineage_01',
            field=models.CharField(blank=True, choices=[('sativa', 'Sativa'), ('hybrid', 'Hybrid'), ('indica', 'Indica')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='strainlineagedetailslistitem',
            name='strain_lineage_02',
            field=models.CharField(blank=True, choices=[('sativa', 'Sativa'), ('hybrid', 'Hybrid'), ('indica', 'Indica')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='strainspecification',
            name='specification_value_label',
            field=models.CharField(blank=True, choices=[('percentage', '%'), ('mg', 'mg')], max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='strainspecification',
            name='title',
            field=models.CharField(blank=True, choices=[('thca', 'THCA '), ('cbd', 'CBD'), ('cbg', 'CBG '), ('thc', 'THC'), ('tac', 'TAC '), ('cbda', 'CBDA '), ('htcv', 'THCV ')], max_length=1000, null=True),
        ),
    ]
