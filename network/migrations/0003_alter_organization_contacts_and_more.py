# Generated by Django 4.1.5 on 2023-01-18 14:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('network', '0002_remove_organization_staff_organization_staff'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='contacts',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='organization', to='network.contact', verbose_name='Контакты'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='debt_to_supplier',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=15, verbose_name='Задолженность перед поставщиком'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='products',
            field=models.ManyToManyField(blank=True, null=True, related_name='organizations', to='network.product', verbose_name='Продукты'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='staff',
            field=models.ManyToManyField(related_name='organization', to=settings.AUTH_USER_MODEL, verbose_name='Сотрудники'),
        ),
    ]