# Generated by Django 4.2.2 on 2024-01-25 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cannabis_db', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000)),
                ('slug', models.SlugField(max_length=1000)),
                ('tagline', models.CharField(max_length=1000)),
                ('description', models.TextField(max_length=400)),
                ('category_icon', models.ImageField(blank=True, null=True, upload_to='media/CANNABIS_DB/CATEGORY_ICONS/')),
            ],
        ),
        migrations.AlterField(
            model_name='comment',
            name='rating',
            field=models.CharField(choices=[('5', '5'), ('4', '4'), ('2', '2'), ('1', '1'), ('3', '3')], max_length=5),
        ),
        migrations.AlterField(
            model_name='dispensary',
            name='shopping_options',
            field=models.CharField(blank=True, choices=[('pickup', 'Pickup'), ('delivery', 'Delivery'), ('all', 'All')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='feelingreport',
            name='type_of_feelings',
            field=models.CharField(choices=[('positive', 'Positive'), ('generic', 'Generic'), ('negative', 'Negative')], max_length=50),
        ),
        migrations.AlterField(
            model_name='rating',
            name='rating',
            field=models.CharField(choices=[('5', '5'), ('4', '4'), ('2', '2'), ('1', '1'), ('3', '3')], max_length=5),
        ),
        migrations.AlterField(
            model_name='strain',
            name='strain_type_label',
            field=models.CharField(choices=[('sativa', 'Sativa'), ('hybrid', 'Hybrid'), ('indica', 'Indica')], max_length=70),
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
            name='specification_name',
            field=models.CharField(choices=[('cbd', 'CBD'), ('cbg', 'CBG '), ('htcv', 'THCV '), ('thc', 'THC')], max_length=1000),
        ),
    ]
