# Generated by Django 4.2.2 on 2024-01-04 17:49

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
                ('aromas_list', models.ManyToManyField(to='cannabis_db.aromasdetails')),
            ],
        ),
        migrations.CreateModel(
            name='AromasListSet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aromas_list_set_name', models.CharField(max_length=1000)),
                ('aromas_list_set', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cannabis_db.aromasdetailslist')),
            ],
        ),
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000)),
                ('slug', models.SlugField(max_length=1000)),
                ('tagline', models.CharField(max_length=1000)),
                ('websiteURL', models.URLField(blank=True, max_length=300, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=300, null=True)),
                ('email_address', models.EmailField(blank=True, max_length=300, null=True)),
                ('brand_logo', models.ImageField(blank=True, null=True, upload_to='media/CANNABIS_DB/BRAND_LOGOS/')),
                ('brand_cover', models.ImageField(blank=True, null=True, upload_to='media/CANNABIS_DB/BRAND_COVERS/')),
                ('description', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('brand_followers', models.ManyToManyField(related_name='strain_brand_followers', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BrandSocialFollows',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_social_follows_name', models.CharField(blank=True, max_length=300, null=True)),
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
            name='DispensarySocialFollowURL',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dispensary_social_profile_name', models.CharField(blank=True, max_length=300, null=True)),
                ('dispensary_social_profile_URL', models.URLField(blank=True, null=True)),
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
                ('feeling_report_list', models.ManyToManyField(to='cannabis_db.feelingreport')),
            ],
        ),
        migrations.CreateModel(
            name='FeelingReportListSet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feeling_report_list_set', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cannabis_db.feelingreportlist')),
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
                ('flavors_list', models.ManyToManyField(to='cannabis_db.flavorsdetails')),
            ],
        ),
        migrations.CreateModel(
            name='FlavorsDetailsListSet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flavors_list_set_name', models.CharField(max_length=1000)),
                ('flavors_list_set', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cannabis_db.flavorsdetailslist')),
            ],
        ),
        migrations.CreateModel(
            name='HelpsWithReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50, null=True)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('description', models.TextField(blank=True, max_length=500, null=True)),
                ('helps_with_icon', models.ImageField(blank=True, max_length=500, null=True, upload_to='media/CANNABIS_DB/HELPS_WITH_ICONS/')),
            ],
        ),
        migrations.CreateModel(
            name='HelpsWithReportList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('helps_with_report_list', models.ManyToManyField(to='cannabis_db.helpswithreport')),
            ],
        ),
        migrations.CreateModel(
            name='HelpsWithReportListSet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('helps_with_report_list', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cannabis_db.helpswithreportlist')),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('slug', models.CharField(max_length=300)),
                ('headline', models.CharField(max_length=300)),
                ('rating', models.CharField(choices=[('1', '1'), ('3', '3'), ('5', '5'), ('4', '4'), ('2', '2')], max_length=5)),
                ('comment', models.TextField(blank=True, max_length=500, null=True)),
                ('date_published', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Strain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('strain_type_label', models.CharField(choices=[('hybrid', 'Hybrid'), ('sativa', 'Sativa'), ('indica', 'Indica')], max_length=70)),
                ('title', models.CharField(max_length=50)),
                ('slug', models.SlugField()),
                ('headline', models.CharField(max_length=50)),
                ('description', ckeditor.fields.RichTextField(blank=True, max_length=5000, null=True)),
                ('featured_image', models.ImageField(blank=True, null=True, upload_to='media/CANNABIS_DB/STRAINS/FEATURED_IMAGES/')),
                ('aromas_reports', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cannabis_db.aromaslistset')),
                ('brand', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cannabis_db.brand')),
                ('feelings_reports', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cannabis_db.feelingreportlistset')),
                ('flavor_reports', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cannabis_db.flavorsdetailslistset')),
                ('helps_with_reports', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cannabis_db.helpswithreportlistset')),
            ],
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
            name='StrainGalleryImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_name', models.CharField(max_length=300)),
                ('image', models.ImageField(blank=True, max_length=500, null=True, upload_to='media/CANNABIS_DB/GALLERY_IMAGES/')),
            ],
        ),
        migrations.CreateModel(
            name='StrainGalleryImagesSet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ManyToManyField(to='cannabis_db.straingalleryimage')),
            ],
        ),
        migrations.CreateModel(
            name='StrainKeywords',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keyword', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='StrainKeywordsSet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keywords', models.ManyToManyField(to='cannabis_db.strainkeywords')),
            ],
        ),
        migrations.CreateModel(
            name='StrainLineageDetailsListItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50, null=True)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('strain_lineage_01', models.CharField(blank=True, choices=[('hybrid', 'Hybrid'), ('sativa', 'Sativa'), ('indica', 'Indica')], max_length=50, null=True)),
                ('strain_lineage_value_01', models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True)),
                ('strain_lineage_02', models.CharField(blank=True, choices=[('hybrid', 'Hybrid'), ('sativa', 'Sativa'), ('indica', 'Indica')], max_length=50, null=True)),
                ('strain_lineage_value_02', models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='StrainSpecification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('specification_name', models.CharField(choices=[('thc', 'THC'), ('cbg', 'CBG '), ('cbd', 'CBD')], max_length=1000)),
                ('specification_value', models.DecimalField(decimal_places=2, max_digits=10, max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='StrainSpecifications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('specifications', models.ManyToManyField(to='cannabis_db.strainspecification')),
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
                ('terpene_name', models.CharField(max_length=1000)),
                ('terpene_value', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='TerpeneDetailsList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('terpenes', models.ManyToManyField(to='cannabis_db.terpenedetails')),
            ],
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=300, null=True)),
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
                ('followers', models.ManyToManyField(blank=True, to='cannabis_db.vendor')),
                ('products', models.ManyToManyField(blank=True, related_name='vendor_profile_product', to='cannabis_db.strain')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TerpeneDetailsListSet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('terpene_set_name', models.CharField(max_length=1000)),
                ('terpene_set', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cannabis_db.terpenedetailslist')),
            ],
        ),
        migrations.CreateModel(
            name='StrainSpecificationsSets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('specifications_set_name', models.CharField(max_length=1000)),
                ('specifications_set', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cannabis_db.strainspecifications')),
            ],
        ),
        migrations.CreateModel(
            name='StrainMetas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('strain_meta_title', models.CharField(max_length=60)),
                ('strain_meta_description', models.TextField(max_length=160)),
                ('strain_meta_keywords', models.ForeignKey(max_length=300, on_delete=django.db.models.deletion.CASCADE, to='cannabis_db.strainkeywordsset')),
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
            name='StrainImageGallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gallery_name', models.CharField(max_length=300)),
                ('images', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cannabis_db.straingalleryimagesset')),
            ],
        ),
        migrations.CreateModel(
            name='StrainDetailsListItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
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
        migrations.AddField(
            model_name='strain',
            name='image_galley',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_image_gallery', to='cannabis_db.strainimagegallery'),
        ),
        migrations.AddField(
            model_name='strain',
            name='ratings',
            field=models.ManyToManyField(blank=True, null=True, to='cannabis_db.rating'),
        ),
        migrations.AddField(
            model_name='strain',
            name='strain_details_list',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cannabis_db.straindetailslist'),
        ),
        migrations.AddField(
            model_name='strain',
            name='strain_lineage_details_list',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cannabis_db.strainlineagedetailslist'),
        ),
        migrations.AddField(
            model_name='strain',
            name='strain_metas_set',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='strain_metas', to='cannabis_db.strainmetas'),
        ),
        migrations.AddField(
            model_name='strain',
            name='strain_specifications',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cannabis_db.strainspecificationssets'),
        ),
        migrations.AddField(
            model_name='strain',
            name='strain_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cannabis_db.straintype'),
        ),
        migrations.AddField(
            model_name='strain',
            name='terpenes_reports',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cannabis_db.terpenedetailslistset'),
        ),
        migrations.AddField(
            model_name='strain',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='strain',
            name='vendors',
            field=models.ManyToManyField(to='cannabis_db.vendor'),
        ),
        migrations.AddField(
            model_name='rating',
            name='strain_to_rate',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cannabis_db.strain'),
        ),
        migrations.AddField(
            model_name='rating',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='strain_rating', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='DispensarySocialFollowURLS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('social_profiles_URLS', models.ManyToManyField(blank=True, to='cannabis_db.dispensarysocialfollowurl')),
            ],
        ),
        migrations.CreateModel(
            name='DispensarySocialFollows',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dispensary_social_follows_name', models.CharField(blank=True, max_length=300, null=True)),
                ('social_profiles_URLS', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='cannabis_db.dispensarysocialfollowurls')),
            ],
        ),
        migrations.CreateModel(
            name='Dispensary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000)),
                ('slug', models.SlugField(max_length=1000)),
                ('tagline', models.CharField(max_length=1000)),
                ('websiteURL', models.URLField(blank=True, max_length=300, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=300, null=True)),
                ('email_address', models.EmailField(blank=True, max_length=300, null=True)),
                ('dispensary_logo', models.ImageField(blank=True, null=True, upload_to='media/CANNABIS_DB/BRAND_LOGOS/')),
                ('dispensary_cover_image', models.ImageField(blank=True, null=True, upload_to='media/CANNABIS_DB/BRAND_COVERS/')),
                ('dispensarydescription', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('dispensary_followers', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
                ('dispensary_products', models.ManyToManyField(blank=True, null=True, to='cannabis_db.strain')),
                ('dispensary_social_follow', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cannabis_db.brandsocialfollows')),
            ],
        ),
        migrations.CreateModel(
            name='BrandSocialFollowURLS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('social_profiles_URLS', models.ManyToManyField(blank=True, to='cannabis_db.brandsocialfollowurl')),
            ],
        ),
        migrations.AddField(
            model_name='brandsocialfollows',
            name='social_profiles_URLS',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='cannabis_db.brandsocialfollowurls'),
        ),
        migrations.AddField(
            model_name='brand',
            name='brand_products',
            field=models.ManyToManyField(blank=True, null=True, related_name='brand_strains', to='cannabis_db.strain'),
        ),
        migrations.AddField(
            model_name='brand',
            name='brand_social_follow',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cannabis_db.brandsocialfollows'),
        ),
    ]
