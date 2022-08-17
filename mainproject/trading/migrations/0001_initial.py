# Generated by Django 3.2.4 on 2021-09-23 06:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Trading',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trading_symbol', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='WatchList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Share_Name', models.CharField(max_length=500)),
                ('isClosed', models.CharField(choices=[('yes', 'yes'), ('no', 'no'), ('history', 'history')], max_length=200)),
                ('UserID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserWallet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wallet', models.FloatField()),
                ('Created_By', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='call', to=settings.AUTH_USER_MODEL)),
                ('userid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserSell',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sharename', models.CharField(max_length=100)),
                ('amount', models.FloatField()),
                ('action', models.CharField(choices=[('SELL', 'SELL')], max_length=100)),
                ('sellerid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserBuy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sharename', models.CharField(max_length=100)),
                ('amount', models.FloatField()),
                ('action', models.CharField(choices=[('BUY', 'BUY')], max_length=100)),
                ('buyerid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('sharename', models.CharField(max_length=100)),
                ('quantity', models.IntegerField()),
                ('amount', models.FloatField()),
                ('Brokerage_amount', models.FloatField(blank=True, null=True)),
                ('isClosed', models.CharField(choices=[('yes', 'yes'), ('no', 'no'), ('history', 'history')], default='no', max_length=100)),
                ('Stop_Loss_Value', models.FloatField(blank=True, null=True)),
                ('Target_Value', models.FloatField(blank=True, null=True)),
                ('Close_amount', models.FloatField(blank=True, null=True)),
                ('action', models.CharField(choices=[('BUY', 'BUY'), ('SELL', 'SELL')], max_length=100)),
                ('difference', models.DecimalField(blank=True, decimal_places=5, max_digits=25, null=True)),
                ('Usertransaction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Fund',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_amount', models.IntegerField()),
                ('Created_By_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('UserWalletID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payment', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Brokerage_amount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Brokerage_amount', models.IntegerField()),
                ('Created_By_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('UserWalletID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wallet', to=settings.AUTH_USER_MODEL, unique=True)),
            ],
        ),
    ]
