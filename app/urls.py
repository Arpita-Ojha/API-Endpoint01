from django.urls import path
from .views import BtsMember,BtsInfo

urlpatterns = [
    path('bts/',BtsMember.as_view(),name='bts'),
    path('bts/<int:id>',BtsInfo.as_view())
]
