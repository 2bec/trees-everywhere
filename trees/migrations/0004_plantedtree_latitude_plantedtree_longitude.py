# Generated by Django 4.0.6 on 2022-07-19 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trees', '0003_alter_plantedtree_planted_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='plantedtree',
            name='latitude',
            field=models.DecimalField(decimal_places=6, default=31.1234, max_digits=9),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='plantedtree',
            name='longitude',
            field=models.DecimalField(decimal_places=6, default=76.654345, max_digits=9),
            preserve_default=False,
        ),
    ]