from django.urls import path

from Pantheon.views import pantheon_detail, pantheon_create, pantheon_delete
from Pantheon.views import god_detail, god_create, god_delete

urlpatterns = []

# Detail Views
urlpatterns += [
	path('<int:pk>/', pantheon_detail, name="pantheon-detail"),
	path('god/<int:pk>/', god_detail, name="god-detail"),
]

# Create, Update and Delete Views
urlpatterns += [
	# Pantheons
	path('<int:in_universe>/create/pantheon/', pantheon_create, name="pantheon-create"),
	path('<int:in_universe>/update/pantheon/<int:pk>/', pantheon_create, name="pantheon-update"),
	path('delete/<int:pk>/', pantheon_delete, name="pantheon-delete"),
	
	# Gods
	path('<int:in_pantheon>/create/god/', god_create, name="god-create"),
	path('<int:in_pantheon>/update/god/<int:pk>/', god_create, name="god-update"),
	path('god/delete/<int:pk>/', god_delete, name="god-delete"),
]
