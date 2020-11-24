from django.urls import path

from Project.views import project_list, project_detail, project_create, project_delete

urlpatterns = []

# List and Detail Views
urlpatterns += [
	path('', project_list, name="project-list"),
	path('<int:pk>/', project_detail, name="project-detail"),
]

# Create, Update, and Delete Views
urlpatterns += [
	path('create/', project_create, name="project-create"),
	path('update/<int:pk>/', project_create, name="project-update"),
	path('delete/<int:pk>/', project_delete, name="project-delete"),
]
