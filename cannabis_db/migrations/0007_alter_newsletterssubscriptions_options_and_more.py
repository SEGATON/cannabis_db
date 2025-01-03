# Generated by Django 4.2.2 on 2024-11-20 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cannabis_db', '0006_newsletterssubscriptions_alter_comment_rating_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='newsletterssubscriptions',
            options={'verbose_name_plural': 'Newsletters Subscription EMAILS LIST'},
        ),
        migrations.AlterField(
            model_name='comment',
            name='rating',
            field=models.CharField(choices=[('5', '5'), ('2', '2'), ('4', '4'), ('3', '3'), ('1', '1')], max_length=5),
        ),
        migrations.AlterField(
            model_name='dispensary',
            name='type_of_dispensary',
            field=models.CharField(blank=True, choices=[('recreational', 'Recreational'), ('medical', 'Medical'), ('seed_bank', 'Seed Bank'), ('medical_recreational', 'Medical & Recreational')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='effectreport',
            name='type_of_effects',
            field=models.CharField(choices=[('positive', 'Positive'), ('negative', 'Negative'), ('neutrial', 'Neutrial')], max_length=50),
        ),
        migrations.AlterField(
            model_name='feelingreport',
            name='type_of_feelings',
            field=models.CharField(choices=[('negative', 'Negative'), ('positive', 'Positive'), ('generic', 'Generic')], max_length=50),
        ),
        migrations.AlterField(
            model_name='rating',
            name='rating',
            field=models.CharField(choices=[('5', '5'), ('2', '2'), ('4', '4'), ('3', '3'), ('1', '1')], max_length=5),
        ),
        migrations.AlterField(
            model_name='strain',
            name='strain_type_label',
            field=models.CharField(blank=True, choices=[('indica', 'Indica'), ('hybrid', 'Hybrid'), ('sativa', 'Sativa')], max_length=70, null=True),
        ),
        migrations.AlterField(
            model_name='strainlineagedetailslistitem',
            name='strain_lineage_01',
            field=models.CharField(blank=True, choices=[('indica', 'Indica'), ('hybrid', 'Hybrid'), ('sativa', 'Sativa')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='strainlineagedetailslistitem',
            name='strain_lineage_02',
            field=models.CharField(blank=True, choices=[('indica', 'Indica'), ('hybrid', 'Hybrid'), ('sativa', 'Sativa')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='strainspecification',
            name='title',
            field=models.CharField(blank=True, choices=[('cbda', 'CBDA '), ('cbg', 'CBG '), ('tac', 'TAC '), ('thc', 'THC'), ('thca', 'THCA '), ('htcv', 'THCV '), ('cbd', 'CBD')], max_length=1000, null=True),
        ),
    ]
