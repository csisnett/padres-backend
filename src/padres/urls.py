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
        )
    
]
