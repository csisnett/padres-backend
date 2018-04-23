from django.conf.urls import url
from transactions import views

urlpatterns = [

    url(r'companies/(?P<uuid>[-\w]+)/$',
        views.CompanyDetail.as_view(),
        name='get_delete_update_company'
        ),
    url(r'companies/$',
        views.CompanyList.as_view(),
        name='get_post_companies'
        ),

    url(r'contracts/(?P<uuid>[-\w]+)/$',
        views.ContractDetail.as_view(),
        name='get_delete_update_contract'
        ),
    url(r'contracts/$',
        views.ContractList.as_view(),
        name='get_post_contracts'
        ),

    url(r'bankaccounts/(?P<uuid>[-\w]+)/$',
        views.BankAccountDetail.as_view(),
        name='get_delete_update_bankaccount'
        ),
    url(r'bankaccounts/$',
        views.BankAccountList.as_view(),
        name='get_post_bankaccounts'
        )
    
]
