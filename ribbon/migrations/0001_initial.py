# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-01-22 01:05
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='StripeCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp_created', models.DateTimeField(auto_now_add=True, db_index=True, null=True)),
                ('timestamp_modified', models.DateTimeField(auto_now=True, db_index=True, null=True)),
                ('stripe_id', models.CharField(max_length=128, verbose_name='Stripe ID')),
                ('stripe_response', django.contrib.postgres.fields.jsonb.JSONField()),
                ('last4', models.CharField(max_length=4)),
                ('exp_year', models.PositiveSmallIntegerField()),
                ('exp_month', models.PositiveSmallIntegerField()),
                ('brand', models.CharField(max_length=64)),
                ('country', models.CharField(max_length=64)),
                ('funding', models.CharField(max_length=64)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='StripeCharge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp_created', models.DateTimeField(auto_now_add=True, db_index=True, null=True)),
                ('timestamp_modified', models.DateTimeField(auto_now=True, db_index=True, null=True)),
                ('stripe_id', models.CharField(max_length=128, verbose_name='Stripe ID')),
                ('stripe_response', django.contrib.postgres.fields.jsonb.JSONField()),
                ('amount', models.PositiveIntegerField()),
                ('currency', models.CharField(max_length=10)),
                ('stripe_card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ribbon.StripeCard')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='StripeCustomer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp_created', models.DateTimeField(auto_now_add=True, db_index=True, null=True)),
                ('timestamp_modified', models.DateTimeField(auto_now=True, db_index=True, null=True)),
                ('stripe_id', models.CharField(max_length=128, verbose_name='Stripe ID')),
                ('stripe_response', django.contrib.postgres.fields.jsonb.JSONField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='stripecharge',
            name='stripe_customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ribbon.StripeCustomer'),
        ),
        migrations.AddField(
            model_name='stripecard',
            name='stripe_customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ribbon.StripeCustomer'),
        ),
    ]