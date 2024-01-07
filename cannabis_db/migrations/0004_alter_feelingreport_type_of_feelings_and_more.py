# Generated by Django 4.2.2 on 2024-01-07 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cannabis_db', '0003_strain_dislikes_alter_feelingreport_type_of_feelings_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feelingreport',
            name='type_of_feelings',
            field=models.CharField(choices=[('generic', 'Generic'), ('positive', 'Positive'), ('negative', 'Negative')], max_length=50),
        ),
        migrations.AlterField(
            model_name='rating',
            name='rating',
            field=models.CharField(choices=[('4', '4'), ('2', '2'), ('5', '5'), ('3', '3'), ('1', '1')], max_length=5),
        ),
        migrations.AlterField(
            model_name='strain',
            name='featured_image',
            field=models.ImageField(blank=True, default='media/CANNABIS_DB/STRAINS/FEATURED_IMAGES/default.jpg', null=True, upload_to='media/CANNABIS_DB/STRAINS/FEATURED_IMAGES/'),
        ),
        migrations.AlterField(
            model_name='strain',
            name='headline',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='strain',
            name='strain_type_label',
            field=models.CharField(choices=[('indica', 'Indica'), ('sativa', 'Sativa'), ('hybrid', 'Hybrid')], max_length=70),
        ),
        migrations.AlterField(
            model_name='strainlineagedetailslistitem',
            name='strain_lineage_01',
            field=models.CharField(blank=True, choices=[('indica', 'Indica'), ('sativa', 'Sativa'), ('hybrid', 'Hybrid')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='strainlineagedetailslistitem',
            name='strain_lineage_02',
            field=models.CharField(blank=True, choices=[('indica', 'Indica'), ('sativa', 'Sativa'), ('hybrid', 'Hybrid')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='strainspecification',
            name='specification_name',
            field=models.CharField(choices=[('cbg', 'CBG '), ('htcv', 'THCV '), ('cbd', 'CBD'), ('thc', 'THC')], max_length=1000),
        ),
    ]