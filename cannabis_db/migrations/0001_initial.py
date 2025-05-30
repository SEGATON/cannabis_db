# Generated by Django 4.2.2 on 2025-04-13 23:42

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
            name='AromasDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50, null=True)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('aromas_icon', models.ImageField(blank=True, max_length=500, null=True, upload_to='media/CANNABIS_DB/GALLERY_IMAGES/')),
            ],
        ),
        migrations.CreateModel(
            name='AromasDetailsList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='AromasListSet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('als_UNIQUE_ID', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=1000, null=True)),
                ('slug', models.SlugField(max_length=1000)),
                ('tagline', models.CharField(blank=True, max_length=1000, null=True)),
                ('websiteURL', models.URLField(blank=True, max_length=300, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=300, null=True)),
                ('email_address', models.EmailField(blank=True, max_length=300, null=True)),
                ('brand_logo', models.ImageField(blank=True, null=True, upload_to='media/CANNABIS_DB/BRAND_LOGOS/')),
                ('brand_cover', models.ImageField(blank=True, null=True, upload_to='media/CANNABIS_DB/BRAND_COVERS/')),
                ('description', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('claimed', models.BooleanField(blank=True, default=False, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('date_updated', models.DateTimeField(blank=True, null=True)),
                ('date_deleted', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='BrandSocialFollowURL',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_social_profile_name', models.CharField(blank=True, max_length=300, null=True)),
                ('brand_social_profile_URL', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='BrandSocialFollowURLS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='BrandSocialProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_social_follows_name', models.CharField(blank=True, max_length=300, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000)),
                ('slug', models.SlugField(max_length=1000)),
                ('tagline', models.CharField(max_length=1000)),
                ('description', models.TextField(max_length=400)),
                ('category_icon', models.ImageField(blank=True, null=True, upload_to='media/CANNABIS_DB/CATEGORY_ICONS/')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('date_updated', models.DateTimeField(blank=True, null=True)),
                ('date_deleted', models.DateTimeField(blank=True, null=True)),
            ],
        ),
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
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('date_updated', models.DateTimeField(blank=True, null=True)),
                ('date_deleted', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Dispensary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_of_dispensary', models.CharField(blank=True, choices=[('medical', 'Medical'), ('medical_recreational', 'Medical & Recreational'), ('seed_bank', 'Seed Bank'), ('recreational', 'Recreational')], max_length=50, null=True)),
                ('shopping_options', models.CharField(blank=True, choices=[('delivery', 'Delivery'), ('pickup', 'Pickup'), ('pickup_delivery', 'Pickup/Delivery')], max_length=50, null=True)),
                ('accepted_payment_methods', models.CharField(choices=[('cash', 'Cash'), ('cash_debit_credit', 'Cash, Debit/Credit Cards'), ('debit_credit', 'Debit/Credit Cards')], max_length=50)),
                ('card_types', models.CharField(choices=[('visa', 'Visa'), ('a_e', 'American Express')], max_length=50)),
                ('title', models.CharField(max_length=1000)),
                ('slug', models.SlugField(max_length=1000)),
                ('tagline', models.CharField(blank=True, max_length=1000, null=True)),
                ('websiteURL', models.URLField(blank=True, max_length=300, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=300, null=True)),
                ('email_address', models.EmailField(blank=True, max_length=300, null=True)),
                ('dispensary_logo', models.ImageField(blank=True, default='media/default.jpg/', null=True, upload_to='media/CANNABIS_DB/DISPENSARIES/DISPENSARY_LOGOS/')),
                ('dispensary_cover', models.ImageField(blank=True, null=True, upload_to='media/CANNABIS_DB/DISPENSARY_COVERS/')),
                ('dispensary_description', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('claimed', models.BooleanField(default=False)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('date_updated', models.DateTimeField(blank=True, null=True)),
                ('date_deleted', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'ordering': ('title',),
            },
        ),
        migrations.CreateModel(
            name='DispensarySocialFollows',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dispensary_social_follows_name', models.CharField(blank=True, max_length=300, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='DispensarySocialFollowURL',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dispensary_social_profile_name', models.CharField(blank=True, max_length=300, null=True)),
                ('dispensary_social_profile_URL', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='DispensarySocialFollowURLICON',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spui_UNIQUE_ID', models.CharField(blank=True, max_length=300, null=True)),
                ('social_profiles_URL_icon', models.ImageField(upload_to='media/CANNABIS_DB/DISPENSARIES/DISPENSARIES_SOCIAL_MENUS_ICONS/')),
            ],
        ),
        migrations.CreateModel(
            name='DispensarySocialFollowURLS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='EffectReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_of_effects', models.CharField(choices=[('positive', 'Positive'), ('negative', 'Negative'), ('neutrial', 'Neutrial')], max_length=50)),
                ('title', models.CharField(blank=True, max_length=50, null=True)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('description', models.TextField(blank=True, max_length=500, null=True)),
                ('effect_icon', models.ImageField(blank=True, max_length=500, null=True, upload_to='media/CANNABIS_DB/EFFECTS_ICONS/')),
            ],
            options={
                'verbose_name_plural': 'Effects',
            },
        ),
        migrations.CreateModel(
            name='EffectReportList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('erl_UNIQUE_ID', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='EffectsReportListSet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('erls_UNIQUE_ID', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='FeelingReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_of_feelings', models.CharField(choices=[('generic', 'Generic'), ('positive', 'Positive'), ('negative', 'Negative')], max_length=50)),
                ('title', models.CharField(blank=True, max_length=50, null=True)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('description', models.TextField(blank=True, max_length=500, null=True)),
                ('feeling_icon', models.ImageField(blank=True, max_length=500, null=True, upload_to='media/CANNABIS_DB/FEELINGS_ICONS/')),
            ],
            options={
                'verbose_name_plural': 'Feelings',
            },
        ),
        migrations.CreateModel(
            name='FeelingReportList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('frl_UNIQUE_ID', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='FeelingReportListSet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('frls_UNIQUE_ID', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='FlavorsDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50, null=True)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('flavor_icon', models.ImageField(blank=True, max_length=500, null=True, upload_to='media/CANNABIS_DB/FLAVORS_ICONS/')),
            ],
            options={
                'verbose_name_plural': 'Flavors',
            },
        ),
        migrations.CreateModel(
            name='FlavorsDetailsList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='FlavorsDetailsListSet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flavors_list_set_name', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='GalleryImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.ImageField(blank=True, max_length=500, null=True, upload_to='media/CANNABIS_DB/GALLERY_IMAGES/')),
            ],
        ),
        migrations.CreateModel(
            name='GalleryImagesSet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gis_UNIQUE_ID', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='HelpsWithReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50, null=True)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('description', models.TextField(blank=True, max_length=500, null=True)),
                ('helps_with_icon', models.ImageField(blank=True, default='media/CANNABIS_DB/HELPS_WITH_ICONS/default.jpg/', max_length=500, null=True, upload_to='media/CANNABIS_DB/HELPS_WITH_ICONS/')),
            ],
        ),
        migrations.CreateModel(
            name='HelpsWithReportList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='HelpsWithReportListSet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hw_UNIQUE_ID', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ImageGallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ig_UNIQUE_ID', models.CharField(max_length=300)),
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
            ],
        ),
        migrations.CreateModel(
            name='MetasSet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ms_UNIQUE_ID', models.CharField(max_length=160)),
                ('meta_title', models.CharField(max_length=160)),
                ('meta_slug', models.SlugField(max_length=160)),
                ('meta_description', models.TextField(blank=True, max_length=160, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('date_updated', models.DateTimeField(blank=True, null=True)),
                ('date_deleted', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='NewslettersSubscriptions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=50)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('date_updated', models.DateTimeField(blank=True, null=True)),
                ('date_deleted', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Newsletters Subscription EMAILS LIST',
            },
        ),
        migrations.CreateModel(
            name='Potency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50, null=True)),
                ('slug', models.SlugField()),
                ('description', ckeditor.fields.RichTextField(blank=True, max_length=5000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('slug', models.CharField(max_length=300)),
                ('product_type', models.CharField(choices=[], max_length=50)),
                ('description', ckeditor.fields.RichTextField(blank=True, max_length=5000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Strain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('strain_type_label', models.CharField(blank=True, choices=[('indica', 'Indica'), ('indica-dominant', 'Indica dominant'), ('sativa', 'Sative'), ('sativa-dominant', 'Sativa dominant'), ('sativa-indica-hybrid', 'Sativa indica hybrid'), ('indica-sativa-hybrid', 'Indica sativa hybrid')], max_length=50, null=True)),
                ('status', models.CharField(blank=True, choices=[('draft', 'Draft'), ('published', 'Published'), ('flagged', 'Flagged')], default='draft', max_length=100, null=True)),
                ('title', models.CharField(max_length=50)),
                ('slug', models.SlugField()),
                ('thc', models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True)),
                ('tac', models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True)),
                ('thca', models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True)),
                ('cbd', models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True)),
                ('cnbnd', models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True)),
                ('headline', models.CharField(blank=True, max_length=3000, null=True)),
                ('intro_text', models.CharField(blank=True, max_length=3000, null=True)),
                ('description', ckeditor.fields.RichTextField(blank=True, max_length=5000, null=True)),
                ('featured', models.BooleanField(default=False)),
                ('featured_image', models.ImageField(blank=True, default='media/CANNABIS_DB/STRAINS/FEATURED_IMAGES/default.jpg', null=True, upload_to='media/CANNABIS_DB/STRAINS/FEATURED_IMAGES/')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('date_updated', models.DateTimeField(blank=True, null=True)),
                ('date_deleted', models.DateTimeField(blank=True, null=True)),
                ('author_review', ckeditor.fields.RichTextField(blank=True, max_length=5000, null=True)),
                ('aromas', models.ManyToManyField(blank=True, null=True, to='cannabis_db.aromasdetails')),
                ('aromas_reports', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cannabis_db.aromaslistset')),
                ('bookmarks', models.ManyToManyField(blank=True, null=True, related_name='bookmarked_by', to=settings.AUTH_USER_MODEL)),
                ('brand', models.ManyToManyField(blank=True, null=True, to='cannabis_db.brand')),
                ('dislikes', models.ManyToManyField(blank=True, null=True, related_name='strain_dislikes', to=settings.AUTH_USER_MODEL)),
                ('dispensaries', models.ManyToManyField(blank=True, null=True, to='cannabis_db.dispensary')),
                ('effects_reports', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cannabis_db.effectsreportlistset')),
                ('feelings', models.ManyToManyField(blank=True, null=True, to='cannabis_db.feelingreport')),
                ('feelings_reports', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cannabis_db.feelingreportlistset')),
                ('flavor_reports', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cannabis_db.flavorsdetailslistset')),
                ('flavors', models.ManyToManyField(blank=True, null=True, to='cannabis_db.flavorsdetails')),
                ('helps_with_reports', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cannabis_db.helpswithreportlistset')),
                ('image_gallery', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_image_gallery', to='cannabis_db.imagegallery')),
                ('likes', models.ManyToManyField(blank=True, null=True, related_name='strain_likes', to=settings.AUTH_USER_MODEL)),
                ('may_relieve', models.ManyToManyField(blank=True, null=True, to='cannabis_db.helpswithreport')),
                ('potency', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cannabis_db.potency')),
                ('products', models.ManyToManyField(blank=True, null=True, to='cannabis_db.product')),
            ],
            options={
                'ordering': ('-date_created',),
            },
        ),
        migrations.CreateModel(
            name='StrainDetailsListItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50, null=True)),
                ('slug', models.SlugField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='StrainLineageDetailsListItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50, null=True)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('strain_lineage_01', models.CharField(blank=True, choices=[('indica', 'Indica'), ('hybrid', 'Hybrid'), ('sativa', 'Sativa')], max_length=50, null=True)),
                ('strain_lineage_value_01', models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True)),
                ('strain_lineage_02', models.CharField(blank=True, choices=[('indica', 'Indica'), ('hybrid', 'Hybrid'), ('sativa', 'Sativa')], max_length=50, null=True)),
                ('strain_lineage_value_02', models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='StrainSpecification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, choices=[('cbda', 'CBDA '), ('thc', 'THC'), ('cbd', 'CBD'), ('tac', 'TAC '), ('cbg', 'CBG '), ('thca', 'THCA '), ('htcv', 'THCV ')], max_length=1000, null=True)),
                ('specification_value', models.DecimalField(blank=True, decimal_places=2, max_digits=10, max_length=1000, null=True)),
                ('specification_value_label', models.CharField(blank=True, choices=[('percentage', '%'), ('mg', 'mg')], max_length=1000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='StrainType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('slug', models.SlugField()),
            ],
        ),
        migrations.CreateModel(
            name='TerpeneDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('terpene', models.CharField(choices=[('beta-myrcene', 'Beta-Myrcene'), ('ocimene', 'Ocimene'), ('alpha-pinene', 'Alpha-Pinene'), ('myrcene', 'Myrcene'), ('limonene', 'Limonene'), ('caryophyllene', 'Caryophyllene'), ('pinene', 'Pinene'), ('linalool', 'Linalool'), ('humulene', 'Humulene'), ('ocimene', 'Ocimene'), ('terpinolene', 'Terpinolene'), ('nerolidol', 'Nerolidol'), ('bisabolol', 'Bisabolol'), ('geraniol', 'Geraniol'), ('valencene', 'Valencene'), ('camphene', 'Camphene'), ('farnesene', 'Farnesene'), ('phytol', 'Phytol')], max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='TerpeneIcon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('terpene_icon', models.ImageField(blank=True, default='media/CANNABIS_DB/STRAINS/TERPENES_REPORTS/TERPENE_ICONS/default.jpg/', max_length=500, null=True, upload_to='media/CANNABIS_DB/STRAINS/TERPENES_REPORTS/TERPENE_ICONS/')),
            ],
        ),
        migrations.CreateModel(
            name='TerpeneValue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('terpene_value', models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True)),
                ('terpene_value_lbl', models.CharField(blank=True, choices=[('percentage', '%'), ('milligrams', 'mg')], max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=300, null=True)),
                ('description', ckeditor.fields.RichTextField()),
                ('websiteURL', models.URLField(blank=True, max_length=300, null=True)),
                ('vendor_logo', models.ImageField(blank=True, null=True, upload_to='VENDORS/LOGOS/')),
                ('vendor_cover_image', models.ImageField(blank=True, null=True, upload_to='VENDORS/COVER_IMAGES/')),
                ('phone_number', models.CharField(blank=True, max_length=300, null=True)),
                ('email_address', models.EmailField(blank=True, max_length=300, null=True)),
                ('vendor_is_top_vendor', models.BooleanField(default=False)),
                ('vendor_is_featured', models.BooleanField(default=False)),
                ('vendor_is_bestseller', models.BooleanField(default=False)),
                ('vendor_is_on_sale', models.BooleanField(default=False)),
                ('vendor_high_sell_through', models.BooleanField(default=False)),
                ('headline', models.CharField(max_length=1000)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('date_updated', models.DateTimeField(blank=True, null=True)),
                ('date_deleted', models.DateTimeField(blank=True, null=True)),
                ('followers', models.ManyToManyField(blank=True, to='cannabis_db.vendor')),
                ('products', models.ManyToManyField(blank=True, related_name='vendor_profile_product', to='cannabis_db.strain')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TerpeneProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trpn_UNIQUIE_ID', models.CharField(blank=True, max_length=50, null=True)),
                ('title', models.CharField(blank=True, max_length=50, null=True)),
                ('slug', models.SlugField()),
                ('description', ckeditor.fields.RichTextField(blank=True, max_length=5000, null=True)),
                ('terpene_profile_icon', models.ImageField(blank=True, default='media/CANNABIS_DB/STRAINS/TERPENES_REPORTS/TERPENE_ICONS/default.jpg/', max_length=500, null=True, upload_to='media/CANNABIS_DB/STRAINS/TERPENES_REPORTS/TERPENE_ICONS/')),
                ('terpenes', models.ManyToManyField(to='cannabis_db.terpenedetails')),
            ],
        ),
        migrations.CreateModel(
            name='TerpeneDetailsSet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tds_UNIQUE_ID', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=1000)),
                ('slug', models.SlugField(max_length=1000)),
                ('description', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('terpenes_reports', models.ManyToManyField(to='cannabis_db.terpenedetails')),
            ],
        ),
        migrations.CreateModel(
            name='TerpeneDetailsItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tdsi_UNIQUE_ID', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=1000)),
                ('slug', models.SlugField(max_length=1000)),
                ('description', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('terpenes_reports', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cannabis_db.terpenedetails')),
            ],
        ),
        migrations.AddField(
            model_name='terpenedetails',
            name='terpene_icon',
            field=models.ManyToManyField(blank=True, null=True, to='cannabis_db.terpeneicon'),
        ),
        migrations.AddField(
            model_name='terpenedetails',
            name='terpene_values',
            field=models.ManyToManyField(blank=True, null=True, to='cannabis_db.terpenevalue'),
        ),
        migrations.CreateModel(
            name='StrainSpecificationsSets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sss_UNIQUE_ID', models.CharField(max_length=1000)),
                ('specifications', models.ManyToManyField(blank=True, null=True, to='cannabis_db.strainspecification')),
            ],
        ),
        migrations.CreateModel(
            name='StrainLineageDetailsListItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('strain_lineage_details_list_items', models.ManyToManyField(to='cannabis_db.strainlineagedetailslistitem')),
            ],
        ),
        migrations.CreateModel(
            name='StrainLineageDetailsList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50, null=True)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('strain_lineage_details_list_items', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cannabis_db.strainlineagedetailslistitems')),
            ],
        ),
        migrations.CreateModel(
            name='StrainDetailsListItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sdlis_UNIQUE_ID', models.CharField(blank=True, max_length=50, null=True)),
                ('strain_details_list_items', models.ManyToManyField(to='cannabis_db.straindetailslistitem')),
            ],
        ),
        migrations.CreateModel(
            name='StrainDetailsList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50, null=True)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('strain_details_list_items', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cannabis_db.straindetailslistitems')),
            ],
        ),
    ]
