# Generated by Django 3.2.14 on 2022-08-16 09:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0025_auto_20220816_0953'),
    ]

    operations = [
        migrations.CreateModel(
            name='DepositRequest',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('bank.accountrequest',),
        ),
    ]
