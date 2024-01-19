# Generated by Django 4.2.2 on 2024-01-18 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cannabis_db', '0009_dispensary_type_of_dispensary_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dispensary',
            name='type_of_dispensary',
            field=models.CharField(blank=True, choices=[('medical', 'Medical'), ('Medical_recreational', 'Medical & Recreational'), ('recreational', 'Recreational')], max_length=50, null=True),
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
            field=models.CharField(choices=[('indica', 'Indica'), ('hybrid', 'Hybrid'), ('sativa', 'Sativa')], max_length=70),
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
            name='specification_name',
            field=models.CharField(choices=[('cbg', 'CBG '), ('thc', 'THC'), ('cbd', 'CBD'), ('htcv', 'THCV ')], max_length=1000),
        ),
    ]