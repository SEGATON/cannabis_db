# Generated by Django 4.2.2 on 2024-12-30 18:31

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cannabis_db', '0013_terpenedetails_terpene_value_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='TerpeneDetailsSet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tds_UNIQUE_ID', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=1000)),
                ('slug', models.SlugField(max_length=1000)),
                ('description', ckeditor.fields.RichTextField(blank=True, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='comment',
            name='rating',
            field=models.CharField(choices=[('1', '1'), ('5', '5'), ('4', '4'), ('2', '2'), ('3', '3')], max_length=5),
        ),
        migrations.AlterField(
            model_name='dispensary',
            name='accepted_payment_methods',
            field=models.CharField(choices=[('debit_credit', 'Debit/Credit Cards'), ('cash', 'Cash'), ('cash_debit_credit', 'Cash, Debit/Credit Cards')], max_length=50),
        ),
        migrations.AlterField(
            model_name='dispensary',
            name='shopping_options',
            field=models.CharField(blank=True, choices=[('pickup_delivery', 'Pickup/Delivery'), ('pickup', 'Pickup'), ('delivery', 'Delivery')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='dispensary',
            name='type_of_dispensary',
            field=models.CharField(blank=True, choices=[('medical', 'Medical'), ('seed_bank', 'Seed Bank'), ('recreational', 'Recreational'), ('medical_recreational', 'Medical & Recreational')], max_length=50, null=True),
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
            field=models.CharField(choices=[('1', '1'), ('5', '5'), ('4', '4'), ('2', '2'), ('3', '3')], max_length=5),
        ),
        migrations.AlterField(
            model_name='strain',
            name='strain_type_label',
            field=models.CharField(blank=True, choices=[('sativa', 'Sativa'), ('hybrid', 'Hybrid'), ('indica', 'Indica')], max_length=70, null=True),
        ),
        migrations.RemoveField(
            model_name='strain',
            name='terpenes_reports',
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
            field=models.CharField(blank=True, choices=[('thc', 'THC'), ('cbg', 'CBG '), ('cbd', 'CBD'), ('cbda', 'CBDA '), ('tac', 'TAC '), ('htcv', 'THCV '), ('thca', 'THCA ')], max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='strain',
            name='terpenes_reports',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cannabis_db.terpenedetailsset'),
        ),
    ]
