from django.contrib import admin

from main_app.models import Application


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'status', 'type_app', 'created_at', 'updated_at', 'client')
