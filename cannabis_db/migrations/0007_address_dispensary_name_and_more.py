# Generated by Django 4.2.2 on 2024-02-05 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cannabis_db', '0006_alter_comment_rating_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='dispensary_name',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='type_of_address',
            field=models.CharField(choices=[('billing_address', 'Billing address'), ('shipping_address', 'Shipping address'), ('p_o_box_number', 'Post office box number'), ('physical_address', 'Physical Address')], max_length=1000),
        ),
        migrations.AlterField(
            model_name='comment',
            name='rating',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('5', '5'), ('4', '4'), ('3', '3')], max_length=5),
        ),
        migrations.AlterField(
            model_name='dispensary',
            name='shopping_options',
            field=models.CharField(blank=True, choices=[('delivery', 'Delivery'), ('pickup', 'Pickup'), ('all', 'All')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='dispensary',
            name='type_of_dispensary',
            field=models.CharField(blank=True, choices=[('medical', 'Medical'), ('recreational', 'Recreational'), ('Medical_recreational', 'Medical & Recreational')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='rating',
            name='rating',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('5', '5'), ('4', '4'), ('3', '3')], max_length=5),
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
            field=models.CharField(choices=[('cbd', 'CBD'), ('cbg', 'CBG '), ('thc', 'THC'), ('htcv', 'THCV ')], max_length=1000),
        ),
    ]