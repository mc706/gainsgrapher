from django.db import models
from django.contrib.auth.models import User

from uuidfield import UUIDField

from trackers.options import tracker_units


class Tracker(models.Model):
    """
    Track a metric for a User.
    """
    uuid = UUIDField(auto=True)
    user = models.ForeignKey(User)
    name = models.CharField(max_length=16)
    description = models.TextField(max_length=255, help_text="How to take track")
    units = models.CharField(max_length=64, choices=tracker_units)

    def __unicode__(self):
        return self.name


class Entry(models.Model):
    """
    Entries on a Tracker
    """
    uuid = UUIDField(auto=True)
    tracker = models.ForeignKey(Tracker)
    date_created = models.DateTimeField(auto_now_add=True)
    value = models.DecimalField(max_digits=9, decimal_places=2)

    def __unicode__(self):
        return self.tracker.name + '-' + str(self.value)

    def get_value_display(self):
        return str(self.value) + ' ' + self.tracker.units