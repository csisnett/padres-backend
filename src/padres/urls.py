from django.conf.urls import url
from padres import views

urlpatterns = [
    url(r'people/(?P<pk>[0-9]+)$',
        views.PersonDetail.as_view(),
        name='get_delete_update_person'
        ),
    url(r'people/$',
        views.PersonList.as_view(),
        name='get_post_people'
        ),
    url(r'promises/(?P<uuid>[-\w]+)/$',
        views.PromiseDetail.as_view(),
        name='get_delete_update_promise'
        ),
    url(r'promises/$',
        views.PromiseList.as_view(),
        name='get_post_promises'
        )
    
]
