# Generated by Django 4.0.4 on 2022-10-24 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('influencer', '0010_mostsubscribedytchannel_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='MostViewedYTChannel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('url', models.URLField(blank=True, null=True)),
                ('uploads', models.CharField(blank=True, max_length=200, null=True)),
                ('subs', models.CharField(blank=True, max_length=200, null=True)),
                ('TotalViews', models.CharField(blank=True, max_length=2020, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
