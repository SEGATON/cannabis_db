# Generated by Django 4.2.2 on 2024-11-04 02:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cannabis_db', '0025_alter_comment_rating_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='terpenedetailslistset',
            name='terpene_set',
        ),
        migrations.AddField(
            model_name='straingalleryimagesset',
            name='si_UNIQUE_ID',
            field=models.CharField(default=1, max_length=300),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comment',
            name='rating',
            field=models.CharField(choices=[('2', '2'), ('1', '1'), ('3', '3'), ('5', '5'), ('4', '4')], max_length=5),
        ),
        migrations.AlterField(
            model_name='effectreport',
            name='type_of_effects',
            field=models.CharField(choices=[('negative', 'Negative'), ('positive', 'Positive'), ('neutrial', 'Neutrial')], max_length=50),
        ),
        migrations.AlterField(
            model_name='feelingreport',
            name='type_of_feelings',
            field=models.CharField(choices=[('generic', 'Generic'), ('negative', 'Negative'), ('positive', 'Positive')], max_length=50),
        ),
        migrations.AlterField(
            model_name='rating',
            name='rating',
            field=models.CharField(choices=[('2', '2'), ('1', '1'), ('3', '3'), ('5', '5'), ('4', '4')], max_length=5),
        ),
        migrations.RemoveField(
            model_name='strain',
            name='terpenes_reports',
        ),
        migrations.AlterField(
            model_name='straingalleryimagesset',
            name='images',
            field=models.ManyToManyField(blank=True, max_length=500, null=True, to='cannabis_db.straingalleryimage'),
        ),
        migrations.AlterField(
            model_name='strainimagegallery',
            name='images',
            field=models.ForeignKey(blank=True, max_length=500, null=True, on_delete=django.db.models.deletion.CASCADE, to='cannabis_db.straingalleryimagesset'),
        ),
        migrations.AlterField(
            model_name='strainspecification',
            name='title',
            field=models.CharField(blank=True, choices=[('cbd', 'CBD'), ('cbda', 'CBDA '), ('tac', 'TAC '), ('cbg', 'CBG '), ('htcv', 'THCV '), ('thc', 'THC'), ('thca', 'THCA ')], max_length=1000, null=True),
        ),
        migrations.DeleteModel(
            name='TerpeneDetailsList',
        ),
        migrations.DeleteModel(
            name='TerpeneDetailsListSet',
        ),
        migrations.AddField(
            model_name='strain',
            name='terpenes_reports',
            field=models.ManyToManyField(blank=True, null=True, to='cannabis_db.terpenedetails'),
        ),
    ]
