# Generated by Django 2.0.7 on 2018-07-20 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_app', '0002_auto_20180720_1629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(null=True, on_delete='CASCADE', related_name='products', to='shop_app.Category'),
        ),
    ]