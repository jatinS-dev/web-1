# Generated by Django 2.2.4 on 2020-06-30 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0124_profile_sybil_score'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bounty',
            name='web3_type',
            field=models.CharField(choices=[('legacy_gitcoin', 'Legacy Bounty'), ('bounties_network', 'Bounties Network'), ('qr', 'QR Code'), ('web3_modal', 'Web3 Modal')], default='bounties_network', max_length=50),
        ),
        migrations.AlterField(
            model_name='bountyfulfillment',
            name='payout_type',
            field=models.CharField(blank=True, choices=[('bounties_network', 'bounties_network'), ('qr', 'qr'), ('fiat', 'fiat'), ('web3_modal', 'web3_modal')], help_text='payment type used to make the payment', max_length=20, null=True),
        ),
    ]
