# Generated by Django 3.2.9 on 2022-09-17 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20220915_2008'),
    ]

    operations = [
        migrations.AddField(
            model_name='accounts',
            name='otp',
            field=models.IntegerField(default=1234),
            preserve_default=False,
        ),
    ]
