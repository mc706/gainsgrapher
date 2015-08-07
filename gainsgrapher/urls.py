from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView
from gainsgrapher.router import router

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(router.urls)),

    url(r'^robots\.txt$',
        TemplateView.as_view(template_name='robots.txt', content_type='text/plain'), name="robots"),
    url(r'^humans\.txt$',
        TemplateView.as_view(template_name='humans.txt', content_type='text/plain'), name="humans"),
]

