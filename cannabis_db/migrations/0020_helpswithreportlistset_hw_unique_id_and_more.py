# Generated by Django 4.2.2 on 2024-10-29 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cannabis_db', '0019_alter_comment_rating_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='helpswithreportlistset',
            name='hw_UNIQUE_ID',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='rating',
            field=models.CharField(choices=[('1', '1'), ('5', '5'), ('4', '4'), ('2', '2'), ('3', '3')], max_length=5),
        ),
        migrations.AlterField(
            model_name='dispensary',
            name='shopping_options',
            field=models.CharField(blank=True, choices=[('delivery', 'Delivery'), ('all', 'All'), ('pickup', 'Pickup')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='dispensary',
            name='type_of_dispensary',
            field=models.CharField(blank=True, choices=[('medical', 'Medical'), ('Medical_recreational', 'Medical & Recreational'), ('recreational', 'Recreational')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='effectreport',
            name='type_of_effects',
            field=models.CharField(choices=[('neutrial', 'Neutrial'), ('negative', 'Negative'), ('positive', 'Positive')], max_length=50),
        ),
        migrations.AlterField(
            model_name='feelingreport',
            name='type_of_feelings',
            field=models.CharField(choices=[('generic', 'Generic'), ('negative', 'Negative'), ('positive', 'Positive')], max_length=50),
        ),
        migrations.AlterField(
            model_name='rating',
            name='rating',
            field=models.CharField(choices=[('1', '1'), ('5', '5'), ('4', '4'), ('2', '2'), ('3', '3')], max_length=5),
        ),
        migrations.AlterField(
            model_name='strain',
            name='strain_type_label',
            field=models.CharField(choices=[('sativa', 'Sativa'), ('indica', 'Indica'), ('hybrid', 'Hybrid')], max_length=70),
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
            name='title',
            field=models.CharField(blank=True, choices=[('htcv', 'THCV '), ('tac', 'TAC '), ('cbd', 'CBD'), ('cbg', 'CBG '), ('thc', 'THC'), ('cbda', 'CBDA '), ('thca', 'THCA ')], max_length=1000, null=True),
        ),
    ]
