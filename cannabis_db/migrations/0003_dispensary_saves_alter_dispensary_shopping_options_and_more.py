# Generated by Django 4.2.2 on 2024-01-22 07:56

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cannabis_db', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dispensary',
            name='saves',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='dispensary',
            name='shopping_options',
            field=models.CharField(blank=True, choices=[('pickup', 'Pickup'), ('delivery', 'Delivery'), ('all', 'All')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='dispensary',
            name='type_of_dispensary',
            field=models.CharField(blank=True, choices=[('recreational', 'Recreational'), ('Medical_recreational', 'Medical & Recreational'), ('medical', 'Medical')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='feelingreport',
            name='type_of_feelings',
            field=models.CharField(choices=[('positive', 'Positive'), ('generic', 'Generic'), ('negative', 'Negative')], max_length=50),
        ),
        migrations.AlterField(
            model_name='rating',
            name='rating',
            field=models.CharField(choices=[('5', '5'), ('4', '4'), ('1', '1'), ('3', '3'), ('2', '2')], max_length=5),
        ),
        migrations.AlterField(
            model_name='strain',
            name='strain_type_label',
            field=models.CharField(choices=[('hybrid', 'Hybrid'), ('indica', 'Indica'), ('sativa', 'Sativa')], max_length=70),
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
            name='specification_name',
            field=models.CharField(choices=[('htcv', 'THCV '), ('cbd', 'CBD'), ('thc', 'THC'), ('cbg', 'CBG ')], max_length=1000),
        ),
    ]