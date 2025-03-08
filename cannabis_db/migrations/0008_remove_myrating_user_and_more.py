# Generated by Django 4.2.2 on 2025-03-08 02:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cannabis_db', '0007_myrating_user_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myrating',
            name='user',
        ),
        migrations.AlterField(
            model_name='dispensary',
            name='accepted_payment_methods',
            field=models.CharField(choices=[('cash_debit_credit', 'Cash, Debit/Credit Cards'), ('debit_credit', 'Debit/Credit Cards'), ('cash', 'Cash')], max_length=50),
        ),
        migrations.AlterField(
            model_name='dispensary',
            name='shopping_options',
            field=models.CharField(blank=True, choices=[('pickup_delivery', 'Pickup/Delivery'), ('delivery', 'Delivery'), ('pickup', 'Pickup')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='dispensary',
            name='type_of_dispensary',
            field=models.CharField(blank=True, choices=[('medical', 'Medical'), ('seed_bank', 'Seed Bank'), ('medical_recreational', 'Medical & Recreational'), ('recreational', 'Recreational')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='effectreport',
            name='type_of_effects',
            field=models.CharField(choices=[('neutrial', 'Neutrial'), ('negative', 'Negative'), ('positive', 'Positive')], max_length=50),
        ),
        migrations.AlterField(
            model_name='feelingreport',
            name='type_of_feelings',
            field=models.CharField(choices=[('negative', 'Negative'), ('generic', 'Generic'), ('positive', 'Positive')], max_length=50),
        ),
        migrations.AlterField(
            model_name='myrating',
            name='score',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='strainlineagedetailslistitem',
            name='strain_lineage_01',
            field=models.CharField(blank=True, choices=[('sativa', 'Sativa'), ('indica', 'Indica'), ('hybrid', 'Hybrid')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='strainlineagedetailslistitem',
            name='strain_lineage_02',
            field=models.CharField(blank=True, choices=[('sativa', 'Sativa'), ('indica', 'Indica'), ('hybrid', 'Hybrid')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='strainspecification',
            name='specification_value_label',
            field=models.CharField(blank=True, choices=[('mg', 'mg'), ('percentage', '%')], max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='strainspecification',
            name='title',
            field=models.CharField(blank=True, choices=[('thc', 'THC'), ('cbg', 'CBG '), ('thca', 'THCA '), ('cbda', 'CBDA '), ('htcv', 'THCV '), ('tac', 'TAC '), ('cbd', 'CBD')], max_length=1000, null=True),
        ),
    ]
