from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.http import HttpResponse
from django.utils import timezone
from django.views import generic
from django.urls import reverse_lazy
from .models import Event, EventType, Ad, Article
from datetime import datetime, timedelta
from django.utils.safestring import mark_safe

from django.views.generic.detail import DetailView

def index(request):
    template = loader.get_template('website/index.html')
    context = {
        'ad': Ad.objects.last(),
        'articles': Article.objects.filter(status=1),
        'events': Event.objects.all().filter(event_date__gte = timezone.now()).order_by('event_date')[:10],
    }
    print(context)
    return render(request, 'website/index.html', context)
    # return HttpResponse(template.render(context, request=request))


def events(request):
    date = request.GET.get('date')
    eventType = request.GET.get('type')
    keyword = request.GET.get('keyword')
    print(keyword)
    events = Event.objects.all().order_by('event_date')

    if date != '' and date is not None:
        events = events.filter(event_date__gte=date)
    else:
        events = events.filter(event_date__gte=timezone.now())
    if eventType != 'Tous' and eventType is not None:
        events = events.filter(event_type__name=eventType)
    if keyword != '' and keyword is not None:
        events = events.filter(title__icontains=keyword) | events.filter(subtitle=keyword) | events.filter(description__icontains=keyword)
    context = {
        'date': datetime.now(),
        'eventTypes': EventType.objects.all(),
        'events': events
    }

    return render(request, 'website/events.html', context)


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'website/article_detail.html'


class EventDetailView(DetailView):
    model = Event
    template_name = 'website/event_detail.html'