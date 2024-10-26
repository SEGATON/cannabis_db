# Generated by Django 4.2.2 on 2024-03-28 02:13

import django.contrib.auth.validators
from django.db import migrations, models
import django.utils.timezone
import localflavor.us.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('account_type', models.CharField(blank=True, choices=[('vendor_account', 'Vendor account'), ('dropshipper_account', 'Dropshipper account'), ('vendor_and_dropshipper', 'Vendor and dropshipper')], max_length=300, null=True)),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('phone_number', models.CharField(blank=True, max_length=100, null=True)),
                ('business_lega_name', models.CharField(blank=True, max_length=100, null=True)),
                ('d_b_a', models.CharField(blank=True, max_length=100, null=True)),
                ('type_of_business', models.CharField(blank=True, choices=[('sole_proprietor', 'Sole Proprietor'), ('limited_liability_company', 'Limited Liability Company'), ('c_corp', 'C Corporation'), ('s_corp', 'S Corporation'), ('non_profit', 'Nonprofit')], max_length=100, null=True)),
                ('legal_business_address_line_1', models.CharField(blank=True, max_length=100, null=True)),
                ('legal_business_address_line_2', models.CharField(blank=True, max_length=100, null=True)),
                ('legal_business_unit', models.CharField(blank=True, max_length=100, null=True)),
                ('legal_business_city', models.CharField(blank=True, max_length=100, null=True)),
                ('legal_business_state', localflavor.us.models.USStateField(max_length=2)),
                ('legal_business_zip_code', localflavor.us.models.USZipCodeField(max_length=10)),
                ('legal_business_phone_number', models.CharField(blank=True, max_length=100, null=True)),
                ('legal_business_email', models.CharField(blank=True, max_length=100, null=True)),
                ('tax_ID', models.CharField(blank=True, max_length=100, null=True)),
                ('ssn', models.CharField(blank=True, max_length=100, null=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=False)),
                ('application_status', models.CharField(blank=True, choices=[('under_review', 'Under review'), ('pending', 'Pending'), ('active', 'Active'), ('suspended', 'Suspended'), ('terminated', 'Terminated')], max_length=100, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
        ),
    ]
