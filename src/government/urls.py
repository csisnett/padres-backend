from django.conf.urls import url
from government.views import (BillViewSet, LegalCaseViewSet,
PersonBillViewSet, InstitutionViewSet)
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'bills', BillViewSet)
router.register(r'legalcases', LegalCaseViewSet)
router.register(r'personbills', PersonBillViewSet)
router.register(r'institutions', InstitutionViewSet)

urlpatterns = router.urls

"""
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
        ),
     url(r'personbills/(?P<uuid>[-\w]+)/$',
        views.PersonBillDetail.as_view(),
        name='personbill-detail'
        ),
     url(r'personbills/$',
        views.PersonBillList.as_view(),
        name='personbill-list'
        ),
    
]

"""