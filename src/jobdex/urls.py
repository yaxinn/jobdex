from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'card.views.home', name='home'),
    url(r'^about/$', 'card.views.about', name='about'),
    url(r'^report/$', 'card.views.report', name='report'),
    url(r'^login/$', 'user.views.login_view', name='login'),
    url(r'^logout/$', 'user.views.logout_view', name='logout'),
    url(r'^signup/$', 'user.views.signup_view', name='signup'),
    url(r'^api/card/all-cards', 'card.views.get_all_cards', name='get_all_cards'),
    url(r'^api/user/create-card', 'card.views.create_card', name='create_card'),
    url(r'^api/user/remove-card', 'card.views.remove_card', name='remove_card'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
