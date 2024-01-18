# Generated by Django 4.2.2 on 2024-01-18 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cannabis_db', '0011_dispensary_shopping_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='dispensary',
            name='dispensary_brands',
            field=models.ManyToManyField(blank=True, null=True, related_name='dispensary_brands', to='cannabis_db.brand'),
        ),
        migrations.AlterField(
            model_name='dispensary',
            name='dispensary_products',
            field=models.ManyToManyField(blank=True, null=True, related_name='dispensary_products', to='cannabis_db.strain'),
        ),
        migrations.AlterField(
            model_name='dispensary',
            name='type_of_dispensary',
            field=models.CharField(blank=True, choices=[('recreational', 'Recreational'), ('Medical_recreational', 'Medical & Recreational'), ('medical', 'Medical')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='feelingreport',
            name='type_of_feelings',
            field=models.CharField(choices=[('positive', 'Positive'), ('negative', 'Negative'), ('generic', 'Generic')], max_length=50),
        ),
        migrations.AlterField(
            model_name='rating',
            name='rating',
            field=models.CharField(choices=[('2', '2'), ('1', '1'), ('3', '3'), ('5', '5'), ('4', '4')], max_length=5),
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
            name='specification_name',
            field=models.CharField(choices=[('htcv', 'THCV '), ('cbd', 'CBD'), ('thc', 'THC'), ('cbg', 'CBG ')], max_length=1000),
        ),
    ]
