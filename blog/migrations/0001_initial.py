# Generated by Django 4.2.2 on 2025-03-07 21:08

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('slug', models.SlugField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='GalleryImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gallery_image', models.ImageField(upload_to='media/BLOG_POST/GALLERY_IMAGES/')),
            ],
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('gallery_image', models.ManyToManyField(blank=True, null=True, to='blog.galleryimage')),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('slug', models.SlugField(max_length=300)),
                ('introduction', ckeditor.fields.RichTextField(max_length=30000)),
                ('main_paragraph', ckeditor.fields.RichTextField(max_length=30000)),
                ('conclusion', ckeditor.fields.RichTextField(max_length=30000)),
                ('date_published', models.DateTimeField(auto_now_add=True, null=True)),
                ('date_updated', models.DateTimeField()),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='draft', max_length=10)),
                ('featured_image', models.ImageField(blank=True, null=True, upload_to='media/BLOG_POST/FEATURED_IMAGES/')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('category', models.ManyToManyField(blank=True, null=True, to='blog.category')),
            ],
            options={
                'ordering': ('-date_published',),
            },
        ),
    ]
