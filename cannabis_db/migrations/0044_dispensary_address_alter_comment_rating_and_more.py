# Generated by Django 4.2.2 on 2024-11-06 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cannabis_db', '0043_remove_category_category_icon_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='dispensary',
            name='address',
            field=models.ManyToManyField(blank=True, null=True, related_name='dispensary_addresses', to='cannabis_db.address'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='rating',
            field=models.CharField(choices=[('5', '5'), ('3', '3'), ('4', '4'), ('2', '2'), ('1', '1')], max_length=5),
        ),
        migrations.AlterField(
            model_name='dispensary',
            name='dispensary_cover',
            field=models.ImageField(default=1, upload_to='media/CANNABIS_DB/DISPENSARY_COVERS/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='dispensary',
            name='shopping_options',
            field=models.CharField(blank=True, choices=[('delivery', 'Delivery'), ('pickup', 'Pickup'), ('pickup_delivery', 'Pickup/Delivery')], max_length=50, null=True),
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
            field=models.CharField(choices=[('5', '5'), ('3', '3'), ('4', '4'), ('2', '2'), ('1', '1')], max_length=5),
        ),
        migrations.AlterField(
            model_name='strain',
            name='strain_type_label',
            field=models.CharField(blank=True, choices=[('sativa', 'Sativa'), ('indica', 'Indica'), ('hybrid', 'Hybrid')], max_length=70, null=True),
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
            field=models.CharField(blank=True, choices=[('percentage', '%'), ('mg', 'mg')], max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='strainspecification',
            name='title',
            field=models.CharField(blank=True, choices=[('cbd', 'CBD'), ('cbg', 'CBG '), ('thc', 'THC'), ('tac', 'TAC '), ('cbda', 'CBDA '), ('htcv', 'THCV '), ('thca', 'THCA ')], max_length=1000, null=True),
        ),
    ]
