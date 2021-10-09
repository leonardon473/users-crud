from django.urls import path

from .views import UsersListCreateView, UsersRetrieveUpdateDestroyView

urlpatterns = [  # type: ignore
    path('', UsersListCreateView.as_view()),  # type: ignore
    path('<pk>/', UsersRetrieveUpdateDestroyView.as_view()),  # type: ignore
]
