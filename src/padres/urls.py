from django.conf.urls import url
from padres import views

urlpatterns = [
    url(r'people/(?P<uuid>[-\w]+)/$',
        views.PersonDetail.as_view(),
        name='person-detail'
        ),
    url(r'people/$',
        views.PersonList.as_view(),
        name='person-list'
        ),
    url(r'promises/(?P<uuid>[-\w]+)/$',
        views.PromiseDetail.as_view(),
        name='promise-detail'
        ),
    url(r'promises/$',
        views.PromiseList.as_view(),
        name='promise-list'
        ),
    url(r'events/(?P<uuid>[-\w]+)/$',
        views.EventDetail.as_view(),
        name='event-detail'
        ),
    url(r'events/$',
        views.EventList.as_view(),
        name='event-list'
        ),
    url(r'scandals/(?P<uuid>[-\w]+)/$',
        views.ScandalDetail.as_view(),
        name='scandal-detail'
        ),
    url(r'scandals/$',
        views.ScandalList.as_view(),
        name='scandal-list'
        ),
    url(r'resources/(?P<uuid>[-\w]+)/$',
        views.ResourceDetail.as_view(),
        name='resource-detail'
        ),
    url(r'resources/$',
        views.ResourceList.as_view(),
        name='resource-list'
        )
    
]
