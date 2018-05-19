from django.conf.urls import url
from government import views

urlpatterns = [
    url(r'bills/(?P<uuid>[-\w]+)/$',
        views.BillDetail.as_view(),
        name='get_delete_update_bill'
        ),
    url(r'bills/$',
        views.BillList.as_view(),
        name='get_post_bills'
        ),
    url(r'legalcases/(?P<uuid>[-\w]+)/$',
        views.LegalCaseDetail.as_view(),
        name='get_delete_update_legalcase'
        ),
    url(r'legalcases/$',
        views.LegalCaseList.as_view(),
        name='get_post_legalcases'
        )
    
]
