from django.urls import path
from . import views
from .views import ArticleDetailView, EventDetailView

urlpatterns = [
    path('', views.index, name='index'),
    path('events/', views.events, name='events'),
	path('article/<slug:slug>/', ArticleDetailView.as_view(), name='article-detail'),
    path('event/<int:pk>', EventDetailView.as_view(), name='event-detail'),
]

app_name = 'website'

