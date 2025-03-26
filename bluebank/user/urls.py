from django.urls import path
from user.views import sign_up, show_profile

urlpatterns = [
    path('sign-up', sign_up),
    path('show-profile/<int:user_id>', show_profile)
]
