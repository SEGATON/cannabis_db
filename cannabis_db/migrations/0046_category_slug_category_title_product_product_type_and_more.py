# Generated by Django 4.2.2 on 2024-11-08 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cannabis_db', '0045_dispensary_accepted_payment_methods_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.CharField(default=1, max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='category',
            name='title',
            field=models.CharField(default=1, max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='product_type',
            field=models.CharField(choices=[], default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.CharField(default=1, max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='title',
            field=models.CharField(default=1, max_length=300),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comment',
            name='rating',
            field=models.CharField(choices=[('5', '5'), ('2', '2'), ('4', '4'), ('1', '1'), ('3', '3')], max_length=5),
        ),
        migrations.AlterField(
            model_name='dispensary',
            name='accepted_payment_methods',
            field=models.CharField(choices=[('cash_debit_credit', 'Cash, Debit/Credit Cards'), ('debit_credit', 'Debit/Credit Cards'), ('cash', 'Cash')], max_length=50),
        ),
        migrations.AlterField(
            model_name='dispensary',
            name='shopping_options',
            field=models.CharField(blank=True, choices=[('delivery', 'Delivery'), ('pickup', 'Pickup'), ('pickup_delivery', 'Pickup/Delivery')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='dispensary',
            name='type_of_dispensary',
            field=models.CharField(blank=True, choices=[('medical', 'Medical'), ('recreational', 'Recreational'), ('medical_recreational', 'Medical & Recreational')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='effectreport',
            name='type_of_effects',
            field=models.CharField(choices=[('neutrial', 'Neutrial'), ('positive', 'Positive'), ('negative', 'Negative')], max_length=50),
        ),
        migrations.AlterField(
            model_name='feelingreport',
            name='type_of_feelings',
            field=models.CharField(choices=[('generic', 'Generic'), ('positive', 'Positive'), ('negative', 'Negative')], max_length=50),
        ),
        migrations.AlterField(
            model_name='rating',
            name='rating',
            field=models.CharField(choices=[('5', '5'), ('2', '2'), ('4', '4'), ('1', '1'), ('3', '3')], max_length=5),
        ),
        migrations.AlterField(
            model_name='strain',
            name='strain_type_label',
            field=models.CharField(blank=True, choices=[('hybrid', 'Hybrid'), ('sativa', 'Sativa'), ('indica', 'Indica')], max_length=70, null=True),
        ),
        migrations.AlterField(
            model_name='strainlineagedetailslistitem',
            name='strain_lineage_01',
            field=models.CharField(blank=True, choices=[('hybrid', 'Hybrid'), ('sativa', 'Sativa'), ('indica', 'Indica')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='strainlineagedetailslistitem',
            name='strain_lineage_02',
            field=models.CharField(blank=True, choices=[('hybrid', 'Hybrid'), ('sativa', 'Sativa'), ('indica', 'Indica')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='strainspecification',
            name='specification_value_label',
            field=models.CharField(blank=True, choices=[('mg', 'mg'), ('percentage', '%')], max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='strainspecification',
            name='title',
            field=models.CharField(blank=True, choices=[('tac', 'TAC '), ('cbg', 'CBG '), ('thca', 'THCA '), ('cbda', 'CBDA '), ('thc', 'THC'), ('htcv', 'THCV '), ('cbd', 'CBD')], max_length=1000, null=True),
        ),
    ]
