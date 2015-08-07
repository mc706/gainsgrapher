from rest_framework import serializers
from trackers.models import Tracker, Entry


class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry
        fields = (
            'uuid',
            'date_created',
            'value',
        )


class TrackerSerializer(serializers.ModelSerializer):
    entry_set = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='uuid'
     )


    class Meta:
        model = Tracker
        fields = (
            'uuid',
            'name',
            'description',
            'units',
            'entry_set',
        )
