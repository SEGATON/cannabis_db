# Generated by Django 4.2.2 on 2025-02-03 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cannabis_db', '0025_alter_comment_rating_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='rating',
            field=models.CharField(choices=[('4', '4'), ('1', '1'), ('2', '2'), ('5', '5'), ('3', '3')], max_length=5),
        ),
        migrations.AlterField(
            model_name='dispensary',
            name='accepted_payment_methods',
            field=models.CharField(choices=[('cash_debit_credit', 'Cash, Debit/Credit Cards'), ('cash', 'Cash'), ('debit_credit', 'Debit/Credit Cards')], max_length=50),
        ),
        migrations.AlterField(
            model_name='dispensary',
            name='shopping_options',
            field=models.CharField(blank=True, choices=[('delivery', 'Delivery'), ('pickup_delivery', 'Pickup/Delivery'), ('pickup', 'Pickup')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='dispensary',
            name='type_of_dispensary',
            field=models.CharField(blank=True, choices=[('medical', 'Medical'), ('medical_recreational', 'Medical & Recreational'), ('seed_bank', 'Seed Bank'), ('recreational', 'Recreational')], max_length=50, null=True),
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
            field=models.CharField(choices=[('4', '4'), ('1', '1'), ('2', '2'), ('5', '5'), ('3', '3')], max_length=5),
        ),
        migrations.AlterField(
            model_name='strain',
            name='strain_type_label',
            field=models.CharField(blank=True, choices=[('indica', 'Indica'), ('hybrid', 'Hybrid'), ('sativa', 'Sativa')], max_length=70, null=True),
        ),
        migrations.AlterField(
            model_name='strainlineagedetailslistitem',
            name='strain_lineage_01',
            field=models.CharField(blank=True, choices=[('indica', 'Indica'), ('hybrid', 'Hybrid'), ('sativa', 'Sativa')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='strainlineagedetailslistitem',
            name='strain_lineage_02',
            field=models.CharField(blank=True, choices=[('indica', 'Indica'), ('hybrid', 'Hybrid'), ('sativa', 'Sativa')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='strainspecification',
            name='title',
            field=models.CharField(blank=True, choices=[('cbg', 'CBG '), ('cbd', 'CBD'), ('thc', 'THC'), ('tac', 'TAC '), ('cbda', 'CBDA '), ('thca', 'THCA '), ('htcv', 'THCV ')], max_length=1000, null=True),
        ),
    ]
