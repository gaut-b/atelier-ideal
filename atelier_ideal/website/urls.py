from django.urls import path
from . import views
from .views import ArticleDetailView

urlpatterns = [
    path('', views.index, name='index'),
    path('events/', views.events, name='events'),
	path('article/<slug:slug>/', ArticleDetailView.as_view(), name='article-detail'),
]

app_name = 'website'

