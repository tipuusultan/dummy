# Generated by Django 3.2.9 on 2022-09-17 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('influencer', '0002_alter_influencer_profile_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='influencer_profile',
            name='account_name_id',
            field=models.CharField(default='empty', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='influencer_profile',
            name='description',
            field=models.TextField(default='desc'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='influencer_profile',
            name='phone',
            field=models.CharField(default='123', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='influencer_profile',
            name='url',
            field=models.URLField(default='https://lurnify.in'),
            preserve_default=False,
        ),
    ]
