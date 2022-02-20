from django.urls import path

from .views import *

urlpatterns = [
    path(
        '',
        AddSellView.as_view(),
        name = 'AddSell',
    ),
    path(
        'Change_Company_Name/',
        ChangeCompanyName.as_view(),
        name = 'ChangeCompanyName',   
    ),
    path(
        'Change_Company_Name_And_FRC/',
        ChangeCompanyNameAndFRC.as_view(),
        name = 'ChangeCompanyNameAndFRC',   
    )
]
