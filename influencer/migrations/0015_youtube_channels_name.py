# Generated by Django 4.0.4 on 2022-10-30 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('influencer', '0014_alter_youtube_channels_allvideos'),
    ]

    operations = [
        migrations.AddField(
            model_name='youtube_channels',
            name='name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]