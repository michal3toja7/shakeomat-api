# Generated by Django 4.0.8 on 2022-12-01 20:08

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import shakeomat_api.discounts.models._helpers
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DiscountCard',
            fields=[
                ('created_at', models.DateTimeField(
                    auto_now_add=True, verbose_name='Dodano')),
                ('updated_at', models.DateTimeField(
                    auto_now=True, verbose_name='Zaktualizowano')),
                ('id', models.UUIDField(
                    default=uuid.uuid4, editable=False, primary_key=True,
                    serialize=False)),
                ('card_number', models.IntegerField(
                    unique=True, verbose_name='Numer Karty')),
                ('phone_number', models.IntegerField(
                    unique=True, verbose_name='Numer telefonu')),
                ('is_active', models.BooleanField(
                    default=True, verbose_name='Czy Aktywny')),
            ],
            options={
                'verbose_name': 'Karta Klienta',
                'verbose_name_plural': 'Karty Klientów',
            },
        ),
        migrations.CreateModel(
            name='DiscountCoupon',
            fields=[
                ('created_at', models.DateTimeField(
                    auto_now_add=True, verbose_name='Dodano')),
                ('updated_at', models.DateTimeField(
                    auto_now=True, verbose_name='Zaktualizowano')),
                ('id', models.UUIDField(
                    default=uuid.uuid4, editable=False, primary_key=True,
                    serialize=False)),
                ('discount_image', models.FileField(
                    upload_to=shakeomat_api.discounts.models.coupon_image_path,
                    verbose_name='discount_image')),
                ('discount_title', models.CharField(
                    blank=True, max_length=150, null=True,
                    verbose_name='Tytuł')),
                ('discount_description', models.TextField(
                    blank=True, null=True, verbose_name='Opis')),
                ('start_validity_period', models.DateTimeField(
                    default=datetime.datetime.now,
                    verbose_name='Początek obowiązywania')),
                ('end_validity_period', models.DateTimeField(
                    default=shakeomat_api.discounts.models.get_end_of_today,
                    verbose_name='Koniec obowiązywania')),
                ('is_public', models.BooleanField(
                    default=False)),
                ('discount_card', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    to='discounts.discountcard')),
            ],
            options={
                'verbose_name': 'Kupon Zniżkowy',
                'verbose_name_plural': 'Kupony Zniżkowe',
            },
        ),
        migrations.CreateModel(
            name='DiscountStatus',
            fields=[
                ('created_at', models.DateTimeField(
                    auto_now_add=True, verbose_name='Dodano')),
                ('updated_at', models.DateTimeField(
                    auto_now=True, verbose_name='Zaktualizowano')),
                ('id', models.UUIDField(
                    default=uuid.uuid4, editable=False, primary_key=True,
                    serialize=False)),
                ('status', models.CharField(
                    choices=[('NEW', 'Nowy'), ('RESERVED', 'Zarezerwowany'),
                             ('USED', 'Zużyty'),
                             ('EXPIRED', 'Przeterminowany')], default='NEW',
                    max_length=20, verbose_name='Status')),
                ('discount_coupon', models.OneToOneField(
                    on_delete=django.db.models.deletion.CASCADE,
                    related_name='status', to='discounts.discountcoupon')),
                ('reserved_by', models.ForeignKey(
                    blank=True, null=True,
                    on_delete=django.db.models.deletion.CASCADE,
                    related_name='reserved_by', to=settings.AUTH_USER_MODEL,
                    verbose_name='Zarezerwowany przez')),
                ('used_by', models.ForeignKey(
                    blank=True, null=True,
                    on_delete=django.db.models.deletion.CASCADE,
                    related_name='used_by', to=settings.AUTH_USER_MODEL,
                    verbose_name='Zużyty przez')),
            ],
            options={
                'verbose_name': 'Status zniżki',
                'verbose_name_plural': 'Statusy zniżek',
            },
        ),
        migrations.CreateModel(
            name='DiscountCardGroup',
            fields=[
                ('id', models.BigAutoField(
                    auto_created=True, primary_key=True, serialize=False,
                    verbose_name='ID')),
                ('name', models.CharField(
                    max_length=200)),
                ('discount_cards', models.ManyToManyField(
                    blank=True, related_name='card_group',
                    to='discounts.discountcard',
                    verbose_name='Karty klienta')),
                ('owner', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    related_name='owner', to=settings.AUTH_USER_MODEL,
                    verbose_name='Właściciel grupy')),
                ('users', models.ManyToManyField(
                    blank=True, related_name='card_group',
                    to=settings.AUTH_USER_MODEL,
                    verbose_name='Członkowie grupy')),
            ],
            options={
                'verbose_name': 'Grupa kart zniżkowych',
                'verbose_name_plural': 'Grupy kart zniżkowych',
            },
        ),
    ]
