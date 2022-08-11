# Generated by Django 3.2.14 on 2022-08-05 19:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_jalali.db.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('invoice', '0031_auto_20220501_2100'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ReferrerVisitEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'ReferrerVisitEvent',
                'verbose_name_plural': 'ReferrerVisitEvent',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ReferrerSignupEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(choices=[(0, 'New'), (1, 'Processed'), (2, 'Inactive')], default=0)),
                ('user_agent', models.TextField()),
                ('ip_address', models.CharField(max_length=50)),
                ('platform', models.CharField(max_length=50)),
                ('date_created', django_jalali.db.models.jDateTimeField(auto_now_add=True)),
                ('referred', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='referred_signup_events', to=settings.AUTH_USER_MODEL)),
                ('referrer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'ReferrerSignupEvent',
                'verbose_name_plural': 'ReferrerSignupEvents',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ReferrerPurchaseEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(choices=[(0, 'New'), (1, 'Processed'), (2, 'Inactive')], default=0)),
                ('user_agent', models.TextField()),
                ('ip_address', models.CharField(max_length=50)),
                ('platform', models.CharField(max_length=50)),
                ('date_created', django_jalali.db.models.jDateTimeField(auto_now_add=True)),
                ('invoice', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='invoice.invoice')),
                ('referrer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'ReferrerPurchaseEvent',
                'verbose_name_plural': 'ReferrerPurchaseEvents',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PurchaseEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(choices=[(0, 'New'), (1, 'Processed'), (2, 'Inactive')], default=0)),
                ('user_agent', models.TextField()),
                ('ip_address', models.CharField(max_length=50)),
                ('platform', models.CharField(max_length=50)),
                ('date_created', django_jalali.db.models.jDateTimeField(auto_now_add=True)),
                ('invoice', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='invoice.invoice')),
                ('referrer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'PurchaseEvent',
                'verbose_name_plural': 'PurchaseEvents',
                'abstract': False,
            },
        ),
    ]