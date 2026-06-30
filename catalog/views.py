from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from catalog.forms import ChampionForm
from catalog.models import Champion


class ChampionListView(ListView):
    model = Champion
    template_name = "catalog/champion_list.html"
    context_object_name = "champions"
    paginate_by = 12

    def get_queryset(self):
        queryset = Champion.objects.all()

        query = self.request.GET.get("query")

        if query:
            queryset = queryset.filter(
                Q(name__icontains=query)
                | Q(title__icontains=query)
            )

        return queryset


class ChampionDetailView(DetailView):
    model = Champion
    template_name = "catalog/champion_detail.html"


class ChampionCreateView(CreateView):
    model = Champion
    form_class = ChampionForm
    template_name = "catalog/champion_form.html"
    success_url = reverse_lazy("champion-list")


class ChampionUpdateView(UpdateView):
    model = Champion
    form_class = ChampionForm
    template_name = "catalog/champion_form.html"
    success_url = reverse_lazy("champion-list")


class ChampionDeleteView(DeleteView):
    model = Champion
    template_name = "catalog/champion_confirm_delete.html"
    success_url = reverse_lazy("champion-list")
