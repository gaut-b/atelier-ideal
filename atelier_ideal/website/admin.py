from django.contrib import admin
from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.models import FlatPage
from django.contrib.sites.models import Site
from django.utils.translation import gettext_lazy as _
from django.db import models

from ckeditor.widgets import CKEditorWidget
from .models import Event, Ad, Article, EventType
from django import forms

admin.autodiscover()
admin.site.unregister(Site)

# class AdminSite(admin.AdminSite):
# 	site_title = 'Atelier Ideal Admin'
# 	site_header = 'Atelier Ideal'
# 	index_title = 'Atelier Ideal Administration'

# Define a new FlatPageAdmin
class FlatPageAdmin(FlatPageAdmin):
    fieldsets = (
        (None, {'fields': ('url', 'title', 'content', 'sites')}),
    )
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget}
    }

    def formfield_for_manytomany(self, db_field, request=None, **kwargs):
    	if db_field.name == "sites":
    		kwargs["initial"] = [Site.objects.get_current()]
    		print(db_field)
    	return super(FlatPageAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)


class EventAdmin(admin.ModelAdmin):
	list_display=('title', 'event_type', 'event_date',)
	list_filter=('event_type', 'event_date')
	search_fields=['title', 'subtitle', 'description']


class ArticleAdmin(admin.ModelAdmin):
	list_display = ('title', 'author', 'status', 'created_on')
	list_filter = ('status',)
	search_fields = ['title', 'content']
	prepopulated_fields = {'slug': ('title',)}

# admin.site = AdminSite()
admin.site.register(Ad)
# admin.site.register(EventType)
admin.site.register(Event, EventAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageAdmin)
# admin.site.register(Question)

