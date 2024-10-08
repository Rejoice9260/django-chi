# Generated by Django 5.1.1 on 2024-09-19 20:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0004_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transaction',
            old_name='Transaction_date',
            new_name='transaction_date',
        ),
        migrations.RenameField(
            model_name='transaction',
            old_name='Transactiontype',
            new_name='transaction_type',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='destination',
        ),
        migrations.AddField(
            model_name='transaction',
            name='destination_account',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='receiver', to='payment.paymentaccount'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='transaction',
            name='reference',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
