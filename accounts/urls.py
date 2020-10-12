from django.urls import path
from django.views.generic.edit import CreateView

from .forms import CustomUserCreationForm
from .views import SignUpView

urlpatterns = [
	path('signup/', SignUpView.as_view(), name="signup"),
]
