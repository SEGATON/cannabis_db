# Generated by Django 4.2.2 on 2024-11-08 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cannabis_db', '0048_category_category_icon_alter_comment_rating_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='strain',
            name='featured',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='comment',
            name='rating',
            field=models.CharField(choices=[('5', '5'), ('1', '1'), ('2', '2'), ('4', '4'), ('3', '3')], max_length=5),
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
            model_name='dispensary',
            name='type_of_dispensary',
            field=models.CharField(blank=True, choices=[('recreational', 'Recreational'), ('medical', 'Medical'), ('medical_recreational', 'Medical & Recreational')], max_length=50, null=True),
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
            model_name='rating',
            name='rating',
            field=models.CharField(choices=[('5', '5'), ('1', '1'), ('2', '2'), ('4', '4'), ('3', '3')], max_length=5),
        ),
        migrations.AlterField(
            model_name='strain',
            name='strain_type_label',
            field=models.CharField(blank=True, choices=[('hybrid', 'Hybrid'), ('indica', 'Indica'), ('sativa', 'Sativa')], max_length=70, null=True),
        ),
        migrations.AlterField(
            model_name='strainlineagedetailslistitem',
            name='strain_lineage_01',
            field=models.CharField(blank=True, choices=[('hybrid', 'Hybrid'), ('indica', 'Indica'), ('sativa', 'Sativa')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='strainlineagedetailslistitem',
            name='strain_lineage_02',
            field=models.CharField(blank=True, choices=[('hybrid', 'Hybrid'), ('indica', 'Indica'), ('sativa', 'Sativa')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='strainspecification',
            name='specification_value_label',
            field=models.CharField(blank=True, choices=[('mg', 'mg'), ('percentage', '%')], max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='strainspecification',
            name='title',
            field=models.CharField(blank=True, choices=[('htcv', 'THCV '), ('thca', 'THCA '), ('cbg', 'CBG '), ('thc', 'THC'), ('tac', 'TAC '), ('cbd', 'CBD'), ('cbda', 'CBDA ')], max_length=1000, null=True),
        ),
    ]
