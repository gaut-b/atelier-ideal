from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# class Question(models.Model):
#     question_text = models.CharField(max_length=200)
#     pub_date = models.DateTimeField('date published')

#     def __str__(self):
#         return self.question_text


# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)

#     def __str__(self):
#         return self.choice_text

STATUS = (
    (0, 'DRAFT'),
    (1, 'PUBLISHED')
)

class Article(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=20, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='article')
    updated_on = models.DateTimeField(auto_now=True)
    content = RichTextUploadingField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)

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


class Event(models.Model):
    title = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=50, blank=True)
    event_type = models.ForeignKey(EventType, on_delete=models.PROTECT)
    event_date = models.DateTimeField()
    description = RichTextUploadingField(blank=True, null=True)
    photo = models.ImageField(null=True, blank=True)


    def __str__(self):
        return self.title

class Ad(models.Model):
    title = models.CharField(max_length=50)
    content = RichTextUploadingField(blank=True, null=True)

    def __str__(self):
        return self.title