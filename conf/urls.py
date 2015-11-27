from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

from django_restify.restify import router

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gettingstarted.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^api/v1/', include(router.urls)),

    # url(r'^db', hello.views.db, name='db'),
    url(r'^admin/', include(admin.site.urls)),

)

urlpatterns = urlpatterns + [
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
