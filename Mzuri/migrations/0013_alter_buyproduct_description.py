# Generated by Django 5.0.7 on 2024-11-24 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mzuri', '0012_buyproduct_productimage_delete_buy_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buyproduct',
            name='description',
            field=models.TextField(blank=True, max_length=250),
        ),
    ]
