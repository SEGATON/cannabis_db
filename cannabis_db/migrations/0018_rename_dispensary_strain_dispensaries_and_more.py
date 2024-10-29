# Generated by Django 4.2.2 on 2024-10-29 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cannabis_db', '0017_strain_date_updated_alter_comment_rating_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='strain',
            old_name='dispensary',
            new_name='dispensaries',
        ),
        migrations.AlterField(
            model_name='comment',
            name='rating',
            field=models.CharField(choices=[('3', '3'), ('4', '4'), ('2', '2'), ('1', '1'), ('5', '5')], max_length=5),
        ),
        migrations.AlterField(
            model_name='dispensary',
            name='shopping_options',
            field=models.CharField(blank=True, choices=[('pickup', 'Pickup'), ('delivery', 'Delivery'), ('all', 'All')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='dispensary',
            name='type_of_dispensary',
            field=models.CharField(blank=True, choices=[('medical', 'Medical'), ('Medical_recreational', 'Medical & Recreational'), ('recreational', 'Recreational')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='effectreport',
            name='type_of_effects',
            field=models.CharField(choices=[('neutrial', 'Neutrial'), ('positive', 'Positive'), ('negative', 'Negative')], max_length=50),
        ),
        migrations.AlterField(
            model_name='feelingreport',
            name='type_of_feelings',
            field=models.CharField(choices=[('generic', 'Generic'), ('positive', 'Positive'), ('negative', 'Negative')], max_length=50),
        ),
        migrations.AlterField(
            model_name='rating',
            name='rating',
            field=models.CharField(choices=[('3', '3'), ('4', '4'), ('2', '2'), ('1', '1'), ('5', '5')], max_length=5),
        ),
        migrations.AlterField(
            model_name='strainspecification',
            name='title',
            field=models.CharField(blank=True, choices=[('cbg', 'CBG '), ('htcv', 'THCV '), ('cbd', 'CBD'), ('thc', 'THC'), ('tac', 'TAC '), ('cbda', 'CBDA '), ('thca', 'THCA ')], max_length=1000, null=True),
        ),
    ]