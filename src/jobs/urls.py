from django.conf.urls import url
from jobs.views import (CongressJobViewSet, GovernmentJobViewSet,
InstitutionViewSet, PrivateJobViewSet)
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'congressjobs', CongressJobViewSet)
router.register(r'governmentjobs', GovernmentJobViewSet)
router.register(r'privatejobs', PrivateJobViewSet)

urlpatterns = router.urls






"""
Saved just in case

urlpatterns = [
    url(r'congressjobs/(?P<uuid>[-\w]+)/$',
        views.CongressJobDetail.as_view(),
        name='get_delete_update_congressjob'
        ),
    url(r'congressjobs/$',
        views.CongressJobList.as_view(),
        name='get_post_congressjobs'
        ),
    url(r'institutions/(?P<uuid>[-\w]+)/$',
        views.InstitutionDetail.as_view(),
        name='get_delete_update_institution'
        ),
    url(r'institutions/$',
        views.InstitutionList.as_view(),
        name='get_post_institutions'
        ),

    url(r'governmentjobs/(?P<uuid>[-\w]+)/$',
        views.GovernmentJobDetail.as_view(),
        name='get_delete_update_governmentjob'
        ),
    url(r'governmentjobs/$',
        views.GovernmentJobList.as_view(),
        name='get_post_governmentjobs'
        ),

    url(r'privatejobs/(?P<uuid>[-\w]+)/$',
        views.PrivateJobDetail.as_view(),
        name='get_delete_update_privatejob'
        ),
    url(r'privatejobs/$',
        views.PrivateJobList.as_view(),
        name='get_post_privatejobs'
        )
    
]

"""