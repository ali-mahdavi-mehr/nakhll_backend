# Generated by Django 3.1.6 on 2021-09-18 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nakhll_market', '0107_product_post_range_cities'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='post_range_cities',
            field=models.ManyToManyField(related_name='products', to='nakhll_market.BigCity', verbose_name='شهرهای قابل ارسال'),
        ),
    ]