# Generated by Django 3.2.14 on 2022-07-31 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0007_auto_20220730_1540'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountrequest',
            name='request_type',
            field=models.IntegerField(choices=[(0, 'درخواست تسویه'), (1, 'واریز'), (2, 'انتقال به حساب حجره دار بابت خرید از حجره')]),
        ),
    ]
