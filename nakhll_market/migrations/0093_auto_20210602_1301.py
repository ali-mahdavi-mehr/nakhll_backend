# Generated by Django 3.1.6 on 2021-06-02 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nakhll_market', '0092_delete_user_view'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slider',
            name='Location',
            field=models.IntegerField(verbose_name='مکان اسلایدر'),
        ),
    ]