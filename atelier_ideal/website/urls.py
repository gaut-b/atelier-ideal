from django.urls import path
from . import views
from .views import ArticleDetailView

urlpatterns = [
    path('', views.index, name='index'),
    path('<slug:slug>/', ArticleDetailView.as_view(), name='article-detail'),
    path('events/', views.events, name='events'),
]

app_name = 'website'
