# Generated by Django 4.2.1 on 2023-06-18 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchases', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase',
            name='stripe_checkout_session_id',
            field=models.CharField(blank=True, max_length=220, null=True),
        ),
        migrations.AddField(
            model_name='purchase',
            name='stripe_price',
            field=models.IntegerField(default=0),
        ),
    ]
