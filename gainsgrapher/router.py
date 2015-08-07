from rest_framework_extensions.routers import NestedRouterMixin
from rest_framework.routers import DefaultRouter

from trackers import views as tracker_views


class SimpleRouterWithNesting(NestedRouterMixin, DefaultRouter):
    pass


router = SimpleRouterWithNesting()

router.register('trackers', tracker_views.TrackerViewSet) \
    .register(r'entries', tracker_views.EntryViewSet, 'tracker-entries', parents_query_lookups=['uuid'])

