# Generated by Django 4.2.2 on 2024-02-06 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cannabis_db', '0009_brand_dispensary_alter_comment_rating_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='brand',
            name='dispensary',
        ),
        migrations.AlterField(
            model_name='comment',
            name='rating',
            field=models.CharField(choices=[('5', '5'), ('1', '1'), ('4', '4'), ('3', '3'), ('2', '2')], max_length=5),
        ),
        migrations.AlterField(
            model_name='dispensary',
            name='shopping_options',
            field=models.CharField(blank=True, choices=[('all', 'All'), ('pickup', 'Pickup'), ('delivery', 'Delivery')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='dispensary',
            name='type_of_dispensary',
            field=models.CharField(blank=True, choices=[('Medical_recreational', 'Medical & Recreational'), ('recreational', 'Recreational'), ('medical', 'Medical')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='feelingreport',
            name='type_of_feelings',
            field=models.CharField(choices=[('negative', 'Negative'), ('generic', 'Generic'), ('positive', 'Positive')], max_length=50),
        ),
        migrations.AlterField(
            model_name='rating',
            name='rating',
            field=models.CharField(choices=[('5', '5'), ('1', '1'), ('4', '4'), ('3', '3'), ('2', '2')], max_length=5),
        ),
        migrations.AlterField(
            model_name='strainspecification',
            name='specification_name',
            field=models.CharField(choices=[('cbd', 'CBD'), ('thc', 'THC'), ('htcv', 'THCV '), ('cbg', 'CBG ')], max_length=1000),
        ),
        migrations.AddField(
            model_name='brand',
            name='dispensary',
            field=models.ManyToManyField(blank=True, null=True, to='cannabis_db.dispensary'),
        ),
    ]
