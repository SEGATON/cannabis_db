# Generated by Django 4.2.2 on 2024-01-03 11:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cannabis_db', '0002_strain_user_alter_feelingreport_type_of_feelings_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendor',
            name='ratings',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cannabis_db.rating'),
        ),
        migrations.AlterField(
            model_name='feelingreport',
            name='type_of_feelings',
            field=models.CharField(choices=[('positive', 'Positive'), ('negative', 'Negative')], max_length=50),
        ),
        migrations.AlterField(
            model_name='rating',
            name='date_updated',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='rating',
            name='rating',
            field=models.CharField(choices=[('2', '2'), ('3', '3'), ('1', '1'), ('5', '5'), ('4', '4')], max_length=5),
        ),
        migrations.AlterField(
            model_name='strain',
            name='strain_type_label',
            field=models.CharField(choices=[('indica', 'Indica'), ('sativa', 'Sativa'), ('hybrid', 'Hybrid')], max_length=70),
        ),
        migrations.AlterField(
            model_name='strainspecification',
            name='specification_name',
            field=models.CharField(choices=[('cbd', 'CBD'), ('thc', 'THC'), ('cbg', 'CBG ')], max_length=1000),
        ),
    ]
