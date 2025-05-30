# Generated by Django 4.2.2 on 2025-04-13 23:42

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Attribute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.CharField(max_length=255)),
                ('attribute_details', ckeditor.fields.RichTextField(blank=True, max_length=300, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='AttributesSet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('as_UNIQUE_ID', models.CharField(max_length=255)),
                ('attributes', models.ManyToManyField(blank=True, null=True, to='catalog.attribute')),
            ],
        ),
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.CharField(max_length=255)),
                ('description', ckeditor.fields.RichTextField(blank=True, max_length=1000, null=True)),
                ('brand_logo', models.ImageField(default='', upload_to='media/DJANGO_ECOMMERCE/BRANDS/BRANDS_LOGOS/')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField()),
                ('date_deleted', models.DateTimeField()),
            ],
            options={
                'verbose_name_plural': 'Brands',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.CharField(max_length=255)),
                ('description', ckeditor.fields.RichTextField(blank=True, max_length=1000, null=True)),
                ('category_icon', models.ImageField(blank=True, default='', null=True, upload_to='media/DJANGO_ECOMMERCE/CATEGORIES/CATEGORY_ICONS/')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField()),
                ('date_deleted', models.DateTimeField()),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='catalog.category')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DescriptionList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dl_UNIQUE_ID', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='DescriptionListItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.CharField(max_length=255)),
                ('description_list_item_short_description', ckeditor.fields.RichTextField(blank=True, max_length=30000, null=True)),
                ('description_list_item_image', models.ImageField(default='', upload_to='media/DJANGO_ECOMMERCE/PRODUCTS/DESCRIPTION_LIST_ITEMS_IMAGES/')),
            ],
        ),
        migrations.CreateModel(
            name='Keywords',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keyword', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='KeywordsSet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keywords', models.ManyToManyField(to='catalog.keywords')),
            ],
        ),
        migrations.CreateModel(
            name='MetasSet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ms_UNIQUE_ID', models.CharField(max_length=160)),
                ('strain_meta_description', models.TextField(blank=True, max_length=160, null=True)),
                ('strain_meta_keywords', models.ForeignKey(blank=True, max_length=300, null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.keywordsset')),
            ],
        ),
        migrations.CreateModel(
            name='PricingManagement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_UNIQUE_ID', models.CharField(max_length=255)),
                ('price_sale', models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True)),
                ('price_regular', models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductGalleryImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='', upload_to='media/DJANGO_ECOMMERCE/PRODUCT_GALLERY_IMAGES')),
            ],
        ),
        migrations.CreateModel(
            name='ProductGalleryImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gallery_images', models.ManyToManyField(to='catalog.productgalleryimage')),
            ],
        ),
        migrations.CreateModel(
            name='ProductGalleryImagesSet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pgis_UNIQUE_ID', models.CharField(max_length=255)),
                ('gallery_images_set', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.productgalleryimages')),
            ],
        ),
        migrations.CreateModel(
            name='ProductVariation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.CharField(max_length=255)),
                ('variation_SKU', models.CharField(blank=True, max_length=50, null=True)),
                ('variation_thumbnail', models.ImageField(default='', upload_to='media/DJANGO_ECOMMERCE/PRODUCTS/VARIATIONS/VARIATIONS_THUMBNAILS/')),
                ('variation_short_description', ckeditor.fields.RichTextField(blank=True, max_length=30000, null=True)),
                ('variation_full_description', ckeditor.fields.RichTextField(blank=True, max_length=30000, null=True)),
                ('variation_attributes_set', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.attributesset')),
                ('variation_description_list_set', models.ForeignKey(blank=True, max_length=255, null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.descriptionlist')),
                ('variation_pricing_management', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.pricingmanagement')),
                ('variation_product_gallery', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.productgalleryimagesset')),
            ],
        ),
        migrations.CreateModel(
            name='ShippingSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ss_UNIQUE_ID', models.CharField(max_length=50)),
                ('weight_label', models.CharField(blank=True, choices=[('gm', 'Gm'), ('kg', 'Kg'), ('ounce', 'Oz'), ('lbs', 'Lb')], max_length=50, null=True)),
                ('dimension_length', models.DecimalField(decimal_places=2, max_digits=9)),
                ('dimension_width', models.DecimalField(decimal_places=2, max_digits=9)),
                ('dimension_height', models.DecimalField(decimal_places=2, max_digits=9)),
            ],
        ),
        migrations.CreateModel(
            name='Specification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.CharField(max_length=255)),
                ('specification_label', models.CharField(blank=True, max_length=1000, null=True)),
                ('specification_value', models.CharField(blank=True, max_length=1000, null=True)),
                ('specification_details', ckeditor.fields.RichTextField(blank=True, max_length=300, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='StockManagement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sm_UNIQUE_ID', models.CharField(max_length=255)),
                ('stock_status', models.CharField(choices=[('out_of_stocl', 'Out of stock'), ('in_stock', 'In stock'), ('backordered', 'Backordered')], max_length=255)),
                ('stock_quantity', models.IntegerField()),
                ('low_stock_alert', models.BooleanField(default=False)),
                ('low_stock_alert_min', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='TagsSet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ts_UINIQUE_ID', models.CharField(max_length=50)),
                ('tags', models.ManyToManyField(to='catalog.tag')),
            ],
        ),
        migrations.CreateModel(
            name='SpecificationsSet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.CharField(max_length=255)),
                ('specifications', models.ManyToManyField(blank=True, null=True, to='catalog.specification')),
            ],
        ),
        migrations.CreateModel(
            name='ProductVariationsSet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pvs_UNIQUE_ID', models.CharField(max_length=255)),
                ('variations', models.ManyToManyField(to='catalog.productvariation')),
            ],
        ),
        migrations.AddField(
            model_name='productvariation',
            name='variation_stock_management',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.stockmanagement'),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_status', models.CharField(blank=True, choices=[('inactive', 'Inactive'), ('pending', 'Pending'), ('active', 'Active')], max_length=255, null=True)),
                ('product_visibility', models.CharField(blank=True, choices=[('hidden', 'Hidden'), ('private', 'Private'), ('visible', 'Visible')], max_length=255, null=True)),
                ('product_type', models.CharField(blank=True, choices=[('single_product', 'Single product'), ('variable_product', 'Variable product'), ('digital_product', 'Digital product'), ('dropship_product', 'Dropship product')], max_length=255, null=True)),
                ('title', models.CharField(max_length=255)),
                ('slug', models.CharField(max_length=255)),
                ('short_description', ckeditor.fields.RichTextField(blank=True, max_length=30000, null=True)),
                ('full_description', ckeditor.fields.RichTextField(blank=True, max_length=30000, null=True)),
                ('featured_image', models.ImageField(default='', upload_to='media/DJANGO_ECOMMERCE/PRODUCTS/FEATURED_IMAGES/')),
                ('on_sale', models.BooleanField(default=False)),
                ('featured', models.BooleanField(default=False)),
                ('bestseller', models.BooleanField(default=False)),
                ('product_SKU', models.CharField(blank=True, max_length=255, null=True)),
                ('product_UPC', models.CharField(blank=True, max_length=255, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField()),
                ('date_deleted', models.DateTimeField()),
                ('attributes_set', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.attributesset')),
                ('authors', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
                ('brands', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.brand')),
                ('categories', models.ManyToManyField(blank=True, null=True, to='catalog.category')),
                ('description_list_set', models.ForeignKey(blank=True, max_length=255, null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.descriptionlist')),
                ('pricing_management', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.pricingmanagement')),
                ('product_gallery', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.productgalleryimagesset')),
                ('product_metas_set', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='strain_metas', to='catalog.metasset')),
                ('product_variations', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.productvariationsset')),
                ('shipping_settings', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.shippingsettings')),
                ('specifications_set', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.specificationsset')),
                ('stock_management', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.stockmanagement')),
                ('tags_set', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.tagsset')),
            ],
            options={
                'verbose_name_plural': 'Products',
            },
        ),
        migrations.CreateModel(
            name='DescriptionListItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description_list_items', models.ManyToManyField(blank=True, null=True, to='catalog.descriptionlistitem')),
            ],
        ),
        migrations.AddField(
            model_name='descriptionlist',
            name='description_list_items',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.descriptionlistitems'),
        ),
        migrations.AddField(
            model_name='category',
            name='products',
            field=models.ManyToManyField(blank=True, null=True, to='catalog.product'),
        ),
        migrations.AddField(
            model_name='brand',
            name='products',
            field=models.ManyToManyField(blank=True, null=True, to='catalog.product'),
        ),
    ]
