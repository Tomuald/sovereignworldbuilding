from django.urls import path

from Pantheon.views import pantheon_detail, pantheon_create, pantheon_update, pantheon_delete
from Pantheon.views import god_detail, god_create, god_update, god_delete

urlpatterns = []

# Detail Views
urlpatterns += [
	path('<int:in_project>/pa/<str:name>/', pantheon_detail, name="pantheon-detail"),
	path('<int:in_project>/g/<str:name>/', god_detail, name="god-detail"),
]

# Create, Update and Delete Views
urlpatterns += [
	# Pantheons
	path('<int:in_project>/u/<str:in_universe>/pa/create/new/', pantheon_create, name="pantheon-create"),
	path('<int:in_project>/pa/<str:name>/update/', pantheon_update, name="pantheon-update"),
	path('<int:in_project>/pa/<str:name>/delete/', pantheon_delete, name="pantheon-delete"),

	# Gods
	path('<int:in_project>/pa/<str:in_pantheon>/g/create/new/', god_create, name="god-create"),
	path('<int:in_project>/g/<str:name>/update/', god_update, name="god-update"),
	path('<int:in_project>/g/<str:name>/delete/', god_delete, name="god-delete"),
]
