# Generated by Django 4.2.2 on 2024-11-20 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cannabis_db', '0007_alter_newsletterssubscriptions_options_and_more'),
        ('memberships', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='saved_dispensaries',
            field=models.ManyToManyField(blank=True, null=True, to='cannabis_db.dispensary'),
        ),
    ]
