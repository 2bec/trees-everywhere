# Generated by Django 4.0.6 on 2022-07-18 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trees', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plantedtree',
            name='planted_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='date tree was planted'),
        ),
    ]
