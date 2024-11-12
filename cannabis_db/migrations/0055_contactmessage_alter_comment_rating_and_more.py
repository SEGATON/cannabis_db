# Generated by Django 4.2.2 on 2024-11-12 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cannabis_db', '0054_strain_bookmarks_alter_comment_rating_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000)),
                ('subject', models.CharField(max_length=1000)),
                ('email', models.EmailField(max_length=1000)),
                ('file', models.FileField(upload_to='files')),
                ('phone', models.CharField(max_length=1000)),
                ('message', models.TextField(max_length=400)),
            ],
        ),
        migrations.AlterField(
            model_name='comment',
            name='rating',
            field=models.CharField(choices=[('5', '5'), ('4', '4'), ('1', '1'), ('2', '2'), ('3', '3')], max_length=5),
        ),
        migrations.AlterField(
            model_name='dispensary',
            name='accepted_payment_methods',
            field=models.CharField(choices=[('cash', 'Cash'), ('debit_credit', 'Debit/Credit Cards'), ('cash_debit_credit', 'Cash, Debit/Credit Cards')], max_length=50),
        ),
        migrations.AlterField(
            model_name='dispensary',
            name='type_of_dispensary',
            field=models.CharField(blank=True, choices=[('medical_recreational', 'Medical & Recreational'), ('recreational', 'Recreational'), ('medical', 'Medical')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='feelingreport',
            name='type_of_feelings',
            field=models.CharField(choices=[('generic', 'Generic'), ('positive', 'Positive'), ('negative', 'Negative')], max_length=50),
        ),
        migrations.AlterField(
            model_name='rating',
            name='rating',
            field=models.CharField(choices=[('5', '5'), ('4', '4'), ('1', '1'), ('2', '2'), ('3', '3')], max_length=5),
        ),
        migrations.AlterField(
            model_name='strain',
            name='strain_type_label',
            field=models.CharField(blank=True, choices=[('hybrid', 'Hybrid'), ('indica', 'Indica'), ('sativa', 'Sativa')], max_length=70, null=True),
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
            name='specification_value_label',
            field=models.CharField(blank=True, choices=[('percentage', '%'), ('mg', 'mg')], max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='strainspecification',
            name='title',
            field=models.CharField(blank=True, choices=[('cbg', 'CBG '), ('tac', 'TAC '), ('cbd', 'CBD'), ('htcv', 'THCV '), ('cbda', 'CBDA '), ('thc', 'THC'), ('thca', 'THCA ')], max_length=1000, null=True),
        ),
    ]
