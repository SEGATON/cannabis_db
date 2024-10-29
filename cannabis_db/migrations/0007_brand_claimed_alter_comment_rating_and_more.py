# Generated by Django 4.2.2 on 2024-10-28 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cannabis_db', '0006_alter_comment_rating_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='claimed',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='comment',
            name='rating',
            field=models.CharField(choices=[('5', '5'), ('1', '1'), ('3', '3'), ('4', '4'), ('2', '2')], max_length=5),
        ),
        migrations.AlterField(
            model_name='dispensary',
            name='shopping_options',
            field=models.CharField(blank=True, choices=[('pickup', 'Pickup'), ('delivery', 'Delivery'), ('all', 'All')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='feelingreport',
            name='type_of_feelings',
            field=models.CharField(choices=[('generic', 'Generic'), ('negative', 'Negative'), ('positive', 'Positive')], max_length=50),
        ),
        migrations.AlterField(
            model_name='rating',
            name='rating',
            field=models.CharField(choices=[('5', '5'), ('1', '1'), ('3', '3'), ('4', '4'), ('2', '2')], max_length=5),
        ),
        migrations.AlterField(
            model_name='strainspecification',
            name='specification_name',
            field=models.CharField(choices=[('tac', 'TAC '), ('htcv', 'THCV '), ('cbd', 'CBD'), ('thca', 'THCA '), ('cbg', 'CBG '), ('thc', 'THC'), ('cbda', 'CBDA ')], max_length=1000),
        ),
    ]