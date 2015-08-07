from django.contrib import admin

from trackers.models import Tracker, Entry


@admin.register(Tracker)
class TrackerAdmin(admin.ModelAdmin):
    pass


@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    list_display = ['tracker', 'date_created', 'value']
