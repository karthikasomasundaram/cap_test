# Generated by Django 4.0 on 2021-12-28 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cap_app', '0002_remove_restaurant_place_remove_waiter_restaurant_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecentDownload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('LastDownload', models.FloatField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
