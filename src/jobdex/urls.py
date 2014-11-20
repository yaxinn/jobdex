from django.conf.urls import patterns, include, url
from django.contrib import admin
import settings

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'card.views.home', name='home'),
    url(r'^about/$', 'card.views.about', name='about'),
    url(r'^report/$', 'document.views.report', name='report'),
    url(r'^login/$', 'user.views.login_view', name='login'),
    url(r'^logout/$', 'user.views.logout_view', name='logout'),
    url(r'^signup/$', 'user.views.signup_view', name='signup'),
    url(r'^api/card/all-cards/$', 'card.views.get_all_cards', name='get_all_cards'),
    url(r'^api/document/upload/$', 'document.views.upload_document', name='upload_doc'),
    url(r'^api/document/delete/$', 'document.views.delete_document', name='delete_doc'),
    url(r'^api/user/create-card/$', 'card.views.create_card', name='create_card'),
    url(r'^api/user/remove-card/$', 'card.views.remove_card', name='remove_card'),
    url(r'^api/card/modify-card-status/$', 'card.views.modify_card_status', name="modify_card_status"),
    url(r'^api/user/modify-tag/$', 'card.views.modify_tag', name='modify_tag'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^assets/(?P<path>.*)$', 'django.views.static.serve', {
		'document_root': settings.MEDIA_ROOT}),

    url(r'^admin/', include(admin.site.urls)),
)
