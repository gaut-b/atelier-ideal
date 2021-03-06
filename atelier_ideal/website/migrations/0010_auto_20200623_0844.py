# Generated by Django 3.0.5 on 2020-06-23 06:44

from django.db import migrations, models
import filebrowser.fields


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0009_auto_20200617_1843'),
    ]

    operations = [
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True, verbose_name='Nom')),
                ('slogan', models.CharField(blank=True, max_length=200, null=True, verbose_name='Slogan')),
                ('address', models.CharField(blank=True, max_length=200, null=True, verbose_name='Adresse')),
                ('email', models.EmailField(blank=True, max_length=200, null=True, verbose_name='Email')),
                ('phone', models.CharField(blank=True, max_length=20, null=True, verbose_name='Téléphone')),
                ('facebook', models.URLField(blank=True, null=True, verbose_name='Facebook')),
                ('twitter', models.URLField(blank=True, null=True, verbose_name='Twitter')),
                ('logo', filebrowser.fields.FileBrowseField(blank=True, max_length=200, null=True, verbose_name='Logo')),
                ('banner', filebrowser.fields.FileBrowseField(blank=True, max_length=200, null=True, verbose_name='Bannière')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='ad',
            name='title',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Titre'),
        ),
    ]
