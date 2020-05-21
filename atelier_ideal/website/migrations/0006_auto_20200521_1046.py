# Generated by Django 3.0.5 on 2020-05-21 08:46

from django.db import migrations
import filebrowser.fields


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_auto_20200521_1026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='photo',
            field=filebrowser.fields.FileBrowseField(blank=True, max_length=200, null=True, verbose_name='Photo'),
        ),
        migrations.AlterField(
            model_name='event',
            name='photo',
            field=filebrowser.fields.FileBrowseField(blank=True, max_length=200, null=True, verbose_name='Photo'),
        ),
    ]
