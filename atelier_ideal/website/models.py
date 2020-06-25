from django import forms
from django.db import models
from django.contrib.auth.models import User
from solo.models import SingletonModel
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from filebrowser.fields import FileBrowseField
from filebrowser.base import FileObject


STATUS = (
    (0, 'Brouillon'),
    (1, 'Publié')
)

class Article(models.Model):
    title = models.CharField(verbose_name="Titre", max_length=200, unique=True)
    slug = models.SlugField(max_length=50, unique=True)
    author = models.ForeignKey(User, verbose_name="Auteur", on_delete=models.CASCADE, related_name='article')
    updated_on = models.DateTimeField(verbose_name="Dernière modification", auto_now=True)
    content = RichTextUploadingField(verbose_name="Contenu", blank=True, null=True)
    created_on = models.DateTimeField(verbose_name="Date de création", auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    photo = FileBrowseField(verbose_name="Photo", max_length=200, null=True, blank=True)

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'
        ordering = ['-created_on']

    def __str__(self):
        return self.title


class EventType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Type d'événements"
        verbose_name_plural = "Types d'événements"


class Event(models.Model):
    title = models.CharField(verbose_name="Titre de l'événement", max_length=50)
    subtitle = models.CharField(verbose_name="Sous-titre de l'événement", max_length=50, blank=True)
    infos = models.CharField(verbose_name="Prix / restauration", max_length=50, blank=True, null=True)
    event_type = models.ForeignKey(EventType, verbose_name="Type d'événement", on_delete=models.PROTECT)
    event_date = models.DateTimeField(verbose_name="Date de l'événement",)
    description = RichTextUploadingField(verbose_name="Description de l'événement", blank=True, null=True)
    photo = FileBrowseField(verbose_name="Photo de l'événement", max_length=200, null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'un événement'
        verbose_name_plural = 'Événements'
        ordering = ['-event_date']


class Ad(SingletonModel):
    title = models.CharField(verbose_name="Titre", max_length=50, blank=True, null=True)
    content = RichTextUploadingField(verbose_name="Contenu", blank=True, null=True)

    def __str__(self):
        return self.title or ''

    class Meta:
        verbose_name = 'Annonce'


class Settings(SingletonModel):
    name = models.CharField(verbose_name="Nom", max_length=50, blank=True, null=True)
    slogan = models.CharField(verbose_name="Slogan", max_length=200, blank=True, null=True)
    address = models.CharField(verbose_name="Adresse", max_length=200, blank=True, null=True)
    email = models.EmailField(verbose_name="Email", max_length=200, blank=True, null=True)
    phone = models.CharField(verbose_name="Téléphone", max_length=20, blank=True, null=True)
    facebook = models.URLField(verbose_name="Facebook", max_length=200, blank=True, null=True)
    twitter = models.URLField(verbose_name="Twitter", max_length=200, blank=True, null=True)
    logo = FileBrowseField(verbose_name="Logo", max_length=200, null=True, blank=True)
    banner = FileBrowseField(verbose_name="Bannière", max_length=200, null=True, blank=True)
    favicon = FileBrowseField(verbose_name="Favicon", max_length=200, null=True, blank=True)

    class Meta:
        verbose_name = 'Configuration'