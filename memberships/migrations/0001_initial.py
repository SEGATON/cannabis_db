# Generated by Django 4.2.2 on 2025-04-13 23:42

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cannabis_db', '0001_initial'),
        ('addresses', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('biography', ckeditor.fields.RichTextField(blank=True, max_length=10000, null=True)),
                ('profile_photo', models.ImageField(default='/MEMBERSHIP/PROFILE_PHOTOS/default_profile_photo.png', upload_to='PROFILE_PHOTOS')),
                ('website_url', models.URLField(blank=True, max_length=1000, null=True)),
                ('twitter', models.URLField(blank=True, max_length=1000, null=True)),
                ('facebook', models.URLField(blank=True, max_length=1000, null=True)),
                ('youtube', models.URLField(blank=True, max_length=1000, null=True)),
                ('instagram', models.URLField(blank=True, max_length=1000, null=True)),
                ('verified', models.BooleanField(default=False)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('date_updated', models.DateTimeField(blank=True, null=True)),
                ('date_deleted', models.DateTimeField(blank=True, null=True)),
                ('visibility_options', models.CharField(blank=True, choices=[('public', 'Public'), ('private', 'Private')], default='public', max_length=50, null=True)),
                ('address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='addresses.address')),
                ('bookmarks', models.ManyToManyField(blank=True, null=True, related_name='bookmarked_strains', to='cannabis_db.strain')),
                ('followers', models.ManyToManyField(blank=True, null=True, related_name='profile_follower', to=settings.AUTH_USER_MODEL)),
                ('saved_dispensaries', models.ManyToManyField(blank=True, null=True, to='cannabis_db.dispensary')),
                ('saved_strains', models.ManyToManyField(blank=True, null=True, to='cannabis_db.strain')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
