# Generated by Django 5.0.3 on 2024-05-13 16:43

import ckeditor.fields
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Casino',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('slug', models.SlugField(unique=True)),
                ('small_description', models.TextField(blank=True, null=True)),
                ('description', ckeditor.fields.RichTextField()),
                ('pros', models.TextField(blank=True, null=True, verbose_name='Artılar')),
                ('cons', models.TextField(blank=True, null=True, verbose_name='Eksiler')),
                ('reliable', models.FloatField(blank=True, default=4.95, null=True, verbose_name='Güvenilirlik')),
                ('payment_speed', models.FloatField(blank=True, default=4.95, null=True, verbose_name='Ödeme Hızı')),
                ('support', models.FloatField(blank=True, default=4.95, null=True, verbose_name='Destek')),
                ('playable', models.FloatField(blank=True, default=4.95, null=True, verbose_name='Oynanabilirlik ve Kalite')),
                ('bonusses', models.FloatField(blank=True, default=4.95, null=True, verbose_name='Bonus ve Promosyon')),
                ('url', models.URLField()),
                ('img', models.ImageField(upload_to='')),
                ('sort', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Bonus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('promo_code', models.CharField(blank=True, default='-', max_length=50, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('casino', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='casinoaffiliate_app.casino')),
            ],
        ),
        migrations.CreateModel(
            name='AdminReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, null=True)),
                ('guarantee_support', models.BooleanField(default=False)),
                ('point', models.FloatField()),
                ('casino', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='casinoaffiliate_app.casino')),
            ],
        ),
        migrations.CreateModel(
            name='GameAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', models.FloatField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='GameDeposit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField(default=0)),
                ('trc20', models.TextField(default=0)),
                ('status', models.IntegerField(choices=[(1, 'Onaylandı'), (2, 'Onaylanmadı'), (3, 'Beklemede')], default=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='GameWithdrawal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField(default=0)),
                ('trc20', models.TextField(default=0)),
                ('status', models.IntegerField(choices=[(1, 'Onaylandı'), (2, 'Onaylanmadı'), (3, 'Beklemede')], default=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
