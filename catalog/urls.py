from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView
from django.urls import path

from catalog.views import (
    ChampionCreateView,
    ChampionDeleteView,
    ChampionDetailView,
    ChampionListView,
    ChampionUpdateView,
    RegisterView,
)


urlpatterns = [
    path(
        "",
        ChampionListView.as_view(),
        name="champion-list",
    ),
    path(
        "champions/<int:pk>/",
        ChampionDetailView.as_view(),
        name="champion-detail",
    ),
    path(
        "champions/create/",
        ChampionCreateView.as_view(),
        name="champion-create",
    ),
    path(
        "champions/<int:pk>/update/",
        ChampionUpdateView.as_view(),
        name="champion-update",
    ),
    path(
        "champions/<int:pk>/delete/",
        ChampionDeleteView.as_view(),
        name="champion-delete",
    ),
    path(
        "register/",
        RegisterView.as_view(),
        name="register",
    ),
    path(
        "accounts/login/",
        LoginView.as_view(
            template_name="registration/login.html"
        ),
        name="login",
    ),
    path(
        "logout/",
        auth_views.LogoutView.as_view(),
        name="logout",
    ),
]
