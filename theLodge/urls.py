from django.urls import path

from theLodge.views import theLodge_list_view, shareditemlist_detail, import_itemlist, export_itemlist, delete_shared_itemlist
from theLodge.views import export_universe, import_universe, shareduniverse_detail

urlpatterns = [
    path('', theLodge_list_view, name="theLodge"),
]

# Shared Itemlists
urlpatterns += [
    path('shareditemlist/<int:pk>/', shareditemlist_detail, name="shared-itemlist"),
    path('importitemlist/<int:pk>/', import_itemlist, name="import-itemlist"),
    path('<int:user_id>/exportitemlist/<int:pk>/', export_itemlist, name="export-itemlist"),
    path('shareditemlist/<int:pk>/delete/', delete_shared_itemlist, name="delete-shareditemlist")
]

#Shared Universes
urlpatterns += [
    path('shareduniverse/<int:pk>/', shareduniverse_detail, name="shared-universe"),
    path('<int:user_id>/exportuniverse/<int:pk>/', export_universe, name="export-universe"),
    path('importuniverse/<int:pk>/', import_universe, name="import-universe"),
]
