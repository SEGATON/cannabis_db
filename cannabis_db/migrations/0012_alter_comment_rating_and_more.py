# Generated by Django 4.2.2 on 2024-12-26 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cannabis_db', '0011_strain_cnbnd_strain_lineage_alter_comment_rating_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='rating',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('4', '4'), ('5', '5'), ('3', '3')], max_length=5),
        ),
        migrations.AlterField(
            model_name='dispensary',
            name='accepted_payment_methods',
            field=models.CharField(choices=[('debit_credit', 'Debit/Credit Cards'), ('cash', 'Cash'), ('cash_debit_credit', 'Cash, Debit/Credit Cards')], max_length=50),
        ),
        migrations.AlterField(
            model_name='dispensary',
            name='shopping_options',
            field=models.CharField(blank=True, choices=[('pickup_delivery', 'Pickup/Delivery'), ('pickup', 'Pickup'), ('delivery', 'Delivery')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='dispensary',
            name='type_of_dispensary',
            field=models.CharField(blank=True, choices=[('seed_bank', 'Seed Bank'), ('medical_recreational', 'Medical & Recreational'), ('medical', 'Medical'), ('recreational', 'Recreational')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='rating',
            name='rating',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('4', '4'), ('5', '5'), ('3', '3')], max_length=5),
        ),
        migrations.AlterField(
            model_name='strainspecification',
            name='title',
            field=models.CharField(blank=True, choices=[('tac', 'TAC '), ('cbg', 'CBG '), ('cbda', 'CBDA '), ('cbd', 'CBD'), ('thca', 'THCA '), ('htcv', 'THCV '), ('thc', 'THC')], max_length=1000, null=True),
        ),
    ]