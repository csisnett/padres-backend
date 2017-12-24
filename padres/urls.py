from django.conf.urls import url
from padres import views

urlpatterns = [
    url(r'^api/v1/people/(?P<pk>[0-9]+)$',
        views.get_delete_update_person,
        name='get_delete_update_person'
        ),
    url(r'^api/v1/people/$',
        views.get_post_people,
        name='get_post_people'
        ),

    url(r'^api/v1/jobs/(?P<pk>[0-9]+)$',
        views.get_delete_update_job,
        name='get_delete_update_job'
        ),
    url(r'^api/v1/jobs/$',
        views.get_post_jobs,
        name='get_post_jobs'
        ),

    url(r'^api/v1/companies/(?P<pk>[0-9]+)$',
        views.get_delete_update_company,
        name='get_delete_update_company'
        ),
    url(r'^api/v1/companies/$',
        views.get_post_companies,
        name='get_post_companies'
        ),
    url(r'^api/v1/contracts/(?P<pk>[0-9]+)$',
        views.get_delete_update_contract,
        name='get_delete_update_contract'
        ),
    url(r'^api/v1/contracts/$',
        views.get_post_contracts,
        name='get_post_contracts'
        )
]
