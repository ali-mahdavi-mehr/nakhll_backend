# Generated by Django 3.1.6 on 2021-12-22 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logistic', '0009_auto_20211219_1245'),
    ]

    operations = [
        migrations.AddField(
            model_name='logisticunit',
            name='is_always_active',
            field=models.BooleanField(default=False, help_text='در صورتی که فعال باشد، امکان غیر فعال سازی توسط کاربر وجود ندارد.', verbose_name='همیشه فعال؟'),
        ),
        migrations.AddField(
            model_name='logisticunit',
            name='priority',
            field=models.PositiveIntegerField(default=0, verbose_name='اولویت'),
        ),
        migrations.AddField(
            model_name='logisticunit',
            name='shown_alone',
            field=models.BooleanField(default=False, help_text='در صورتی که فعال باشد، در لیست واحد\u200cهای ارسالی به صورت تنها نمایش داده می\u200cشود.', verbose_name='نمایش به صورت تنها'),
        ),
    ]
