# Generated by Django 5.0 on 2023-12-06 09:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0008_transaction_clientid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='ClientID',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='account.client'),
            preserve_default=False,
        ),
    ]
