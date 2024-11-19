# Generated by Django 4.2.2 on 2024-11-19 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cannabis_db', '0005_remove_dispensary_buy_seeds_strain_seeds_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewslettersSubscriptions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Newsletters Subscription',
            },
        ),
        migrations.AlterField(
            model_name='comment',
            name='rating',
            field=models.CharField(choices=[('3', '3'), ('5', '5'), ('4', '4'), ('1', '1'), ('2', '2')], max_length=5),
        ),
        migrations.AlterField(
            model_name='dispensary',
            name='accepted_payment_methods',
            field=models.CharField(choices=[('cash', 'Cash'), ('cash_debit_credit', 'Cash, Debit/Credit Cards'), ('debit_credit', 'Debit/Credit Cards')], max_length=50),
        ),
        migrations.AlterField(
            model_name='dispensary',
            name='shopping_options',
            field=models.CharField(blank=True, choices=[('pickup', 'Pickup'), ('delivery', 'Delivery'), ('pickup_delivery', 'Pickup/Delivery')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='dispensary',
            name='type_of_dispensary',
            field=models.CharField(blank=True, choices=[('medical_recreational', 'Medical & Recreational'), ('seed_bank', 'Seed Bank'), ('medical', 'Medical'), ('recreational', 'Recreational')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='effectreport',
            name='type_of_effects',
            field=models.CharField(choices=[('positive', 'Positive'), ('neutrial', 'Neutrial'), ('negative', 'Negative')], max_length=50),
        ),
        migrations.AlterField(
            model_name='feelingreport',
            name='type_of_feelings',
            field=models.CharField(choices=[('generic', 'Generic'), ('positive', 'Positive'), ('negative', 'Negative')], max_length=50),
        ),
        migrations.AlterField(
            model_name='potency',
            name='title',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='rating',
            name='rating',
            field=models.CharField(choices=[('3', '3'), ('5', '5'), ('4', '4'), ('1', '1'), ('2', '2')], max_length=5),
        ),
        migrations.AlterField(
            model_name='strain',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='strainspecification',
            name='specification_value_label',
            field=models.CharField(blank=True, choices=[('percentage', '%'), ('mg', 'mg')], max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='strainspecification',
            name='title',
            field=models.CharField(blank=True, choices=[('cbd', 'CBD'), ('tac', 'TAC '), ('cbg', 'CBG '), ('thca', 'THCA '), ('thc', 'THC'), ('cbda', 'CBDA '), ('htcv', 'THCV ')], max_length=1000, null=True),
        ),
    ]