from django.conf.urls import patterns, include, url
from django.contrib import admin
import settings

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'card.views.home', name='home'),
    url(r'^about/$', 'card.views.about', name='about'),
    url(r'^documents/$', 'document.views.documents', name='documents'),
    url(r'^login/$', 'user.views.login_view', name='login'),
    url(r'^logout/$', 'user.views.logout_view', name='logout'),
    url(r'^signup/$', 'user.views.signup_view', name='signup'),
    url(r'^api/card/all-cards/$', 'card.views.get_all_cards', name='get_all_cards'),
    url(r'^api/user/create-deck/$', 'card.views.create_deck', name='create_deck'),
    url(r'^api/card/add-card/$', 'card.views.add_card', name='add_card'),
    url(r'^api/user/remove-card/$', 'card.views.remove_card', name='remove_card'),
    url(r'^api/user/delete-deck/$', 'card.views.delete_deck', name='delete_deck'),

    url(r'^api/card/modify-card-status/$', 'card.views.modify_card_status', name="modify_card_status"),
    url(r'^api/card/edit-contact/$', 'card.views.edit_contact', name="edit_contact"),
    url(r'^api/card/remove-contact/$', 'card.views.remove_contact', name="remove_contact"),
    url(r'^api/card/add-contact/$', 'card.views.add_contact', name="add_contact"),
    url(r'^api/card/get-contacts/$', 'card.views.get_contacts', name="get_contacts"),

    url(r'^api/card/edit-notes/$', 'card.views.edit_notes', name="edit_notes"),
    url(r'^api/card/add-task/$', 'card.views.add_task', name="add_task"),

    url(r'^api/card/add-tag/$', 'card.views.add_tag', name='add_tag'),
    url(r'^api/card/edit-tag/$', 'card.views.edit_tag', name='edit_tag'),
    url(r'^api/card/remove-tag/$', 'card.views.remove_tag', name='remove_tag'),
    url(r'^api/card/get-tags/$', 'card.views.get_tags', name='get_tags'),

    url(r'^api/card/add-document/$', 'card.views.add_document', name='add_document'),

    url(r'^api/document/upload/$', 'document.views.upload_document', name='upload_document'),
    url(r'^api/document/delete/$', 'document.views.delete_document', name='delete_document'),
    url(r'^api/document/get/$', 'document.views.get_documents', name='get_documents'),

    # url(r'^blog/', include('blog.urls')),

    url(r'^assets/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}),

    url(r'^admin/', include(admin.site.urls)),
)
