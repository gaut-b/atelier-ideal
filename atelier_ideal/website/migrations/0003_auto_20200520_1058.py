# Generated by Django 3.0.5 on 2020-05-20 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_UPDATE_SITE_NAME'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='event',
            name='subtitle',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]