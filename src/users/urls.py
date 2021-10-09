from django.urls import path

from .views import UsersListCreateView

urlpatterns = [  # type: ignore
    path('', UsersListCreateView.as_view()),  # type: ignore
]
