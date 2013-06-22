from django.conf.urls import patterns, include, url
import os.path

import tasks.views

from django.conf import settings
from django.contrib import admin
admin.autodiscover()

STATIC_PATH = os.path.abspath(os.path.join(
        os.path.dirname(os.path.abspath(__file__)), '../tasks/static'))

if not os.path.exists(STATIC_PATH):
    raise ValueError(STATIC_PATH)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'minitasks.views.home', name='home'),
    # url(r'^minitasks/', include('minitasks.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', tasks.views.TaskIndex.as_view()),
    url(r'^tasks/$', tasks.views.TaskData.as_view(),
        name='tasks-data'),
    url(r'^claim/$', tasks.views.ClaimTask.as_view(),
        name='tasks-claim'),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT}),
    url(r'^secret-refresh-tasks/$', tasks.views.RefreshTaskData.as_view(),
        name='secret-refresh-tasks'),
)


### Attempt 1:

if settings.DEBUG:
    urlpatterns += patterns('django.contrib.staticfiles.views',
        url(r'^static/(?P<path>.*)$', 'serve'),
    )

