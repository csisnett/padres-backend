from django.conf.urls import url
from padres import views

urlpatterns = [
    url(r'^api/v1/people/(?P<pk>[0-9]+)$',
        views.PersonDetail.as_view(),
        name='get_delete_update_person'
        ),
    url(r'^api/v1/people/$',
        views.PersonList.as_view(),
        name='get_post_people'
        ),

    url(r'^api/v1/jobs/(?P<pk>[0-9]+)$',
        views.JobDetail.as_view(),
        name='get_delete_update_job'
        ),
    url(r'^api/v1/jobs/$',
        views.JobList.as_view(),
        name='get_post_jobs'
        ),

    url(r'^api/v1/companies/(?P<pk>[0-9]+)$',
        views.CompanyDetail.as_view(),
        name='get_delete_update_company'
        ),
    url(r'^api/v1/companies/$',
        views.CompanyList.as_view(),
        name='get_post_companies'
        ),
    url(r'^api/v1/contracts/(?P<pk>[0-9]+)$',
        views.get_delete_update_contract,
        name='get_delete_update_contract'
        ),
    url(r'^api/v1/contracts/$',
        views.get_post_contracts,
        name='get_post_contracts'
        ),
    url(r'api/v1/transactions/(?P<uuid>[-\w]+)/$',
        views.TransactionDetail.as_view(),
        name='get_delete_update_transaction'
        ),
    url(r'api/v1/transactions/$',
        views.TransactionList.as_view(),
        name='get_post_transactions'
        ),
    url(r'api/v1/promises/(?P<uuid>[-\w]+)/$',
        views.PromiseDetail.as_view(),
        name='get_delete_update_promises'
        ),
    url(r'api/v1/promises/$',
        views.PromiseList.as_view(),
        name='get_post_promises'
        )
    
]
