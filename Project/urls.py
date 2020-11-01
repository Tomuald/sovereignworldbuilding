from django.urls import path

from Project.views import project_list, project_detail, project_create, project_delete

urlpatterns = []

# List and Detail Views
urlpatterns += [
	path('', project_list, name="project-list"),
	path('project/<int:pk>/', project_detail, name="project-detail"),
]

# Create, Update, and Delete Views
urlpatterns += [
	path('project/create/', project_create, name="project-create"),
	path('project/update/<int:pk>/', project_create, name="project-update"),
	path('project/delete/<int:pk>/', project_delete, name="project-delete"),
]
