# Generated by Django 4.2.7 on 2023-12-04 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchase_order', '0003_alter_purchaseorder_vendor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaseorder',
            name='order_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
