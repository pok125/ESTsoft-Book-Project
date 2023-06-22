# Generated by Django 4.2.1 on 2023-06-22 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchases', '0002_purchase_stripe_checkout_session_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase',
            name='kakaopay_checkout_tid',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='purchase',
            name='kakaopay_price',
            field=models.IntegerField(default=0),
        ),
    ]
