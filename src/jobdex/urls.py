from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'card.views.home', name='home'),
    url(r'^about/$', 'card.views.about', name='about'),
    url(r'^api/card/all-cards', 'card.views.get_all_cards', name='get_all_cards'),
    url(r'^api/user/create-card', 'card.views.create_card', name='create_card'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
