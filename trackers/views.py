import json
from rest_framework import viewsets, status
from rest_framework.permissions import DjangoModelPermissions
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.response import Response
from rest_framework_extensions.mixins import NestedViewSetMixin

from trackers.models import Tracker, Entry
from trackers.serializers import TrackerSerializer, EntrySerializer


class TrackerViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    """
    API Endpoints for illnesses in a history
    """
    lookup_field = 'uuid'
    queryset = Tracker.objects.all()
    permission_classes = [DjangoModelPermissions]
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    serializer_class = TrackerSerializer
    paginate_by = 100
    page_kwarg = 'page'
    paginate_by_param = 'id'

    def list(self, request, *args, **kwargs):
        trackers = Tracker.objects.filter(user=request.user)
        serializer = TrackerSerializer(trackers, many=True, context={"request": request})
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def create(self, request, *args, **kwargs):
        post = request.POST or json.dumps(request.body)
        tracker = Tracker.objects.create(
            user=request.user,
            name=post.get('name'),
            description=post.get('description', None),
            units=post.get('units')
        )
        serializer = TrackerSerializer(tracker, context={"request": request})
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class EntryViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    lookup_field = 'uuid'
    queryset = Entry.objects.all()
    permission_classes = [DjangoModelPermissions]
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    serializer_class = EntrySerializer
    paginate_by = 100
    page_kwarg = 'page'
    paginate_by_param = 'id'

    def create(self, request, *args, **kwargs):
        post = request.POST or json.dumps(request.body)
        tracker = Tracker.objects.get(uuid=kwargs.get('parent_lookup_uuid'))
        entry = Entry.objects.create(
            tracker=tracker,
            value=post.get("value")
        )
        serializer = EntrySerializer(entry, context={"request": request})
        return Response(serializer.data, status=status.HTTP_201_CREATED)

