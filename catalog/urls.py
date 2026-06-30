from django.urls import path

from catalog.views import (
    ChampionCreateView,
    ChampionDeleteView,
    ChampionDetailView,
    ChampionListView,
    ChampionUpdateView,
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
]
