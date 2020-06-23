from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.auth.models import User
from django.contrib.flatpages.models import FlatPage
from django.contrib.sites.models import Site
from solo.admin import SingletonModelAdmin
from django.utils.translation import gettext_lazy as _
from django.db import models

from ckeditor.widgets import CKEditorWidget
from .models import Event, Ad, Article, EventType, Settings
from django import forms

admin.autodiscover()
admin.site.unregister(Site)
admin.site.unregister(FlatPage)
# Unregister the provided model admin
admin.site.unregister(User)

#Register out own model admin, based on the default UserAdmin
@admin.register(User)
class CustomUserAdmin(UserAdmin):
    readonly_fields = [
        'date_joined',
        'last_login',
    ]

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        is_superuser = request.user.is_superuser
        disabled_fields = set()  # type: Set[str]

        if not is_superuser:
            disabled_fields |= {
                'username',
                'is_superuser',
            }

        for f in disabled_fields:
            if f in form.base_fields:
                form.base_fields[f].disabled = True

        return form


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
	list_display = ('title', 'author', 'status', 'created_on', 'updated_on')
	list_filter = ('status', 'created_on', 'updated_on')
	search_fields = ['title', 'content']
	prepopulated_fields = {'slug': ('title',)}


admin.site.register(EventType)
admin.site.register(Ad, SingletonModelAdmin)
admin.site.register(Settings, SingletonModelAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(FlatPage, FlatPageAdmin)

