from django.urls import path

from theLodge.views import theLodge_list_view, shareditemlist_detail

urlpatterns = []

urlpatterns += [
    path('', theLodge_list_view, name="theLodge"),
    path('shareditemlist/<int:pk>/', shareditemlist_detail, name="shared-itemlist"),
]
