from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from catalog.forms import ChampionForm, UserRegistrationForm
from catalog.models import Champion, Region, Role


class AdminRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_staff


class ChampionListView(ListView):
    model = Champion
    template_name = "catalog/champion_list.html"
    context_object_name = "champions"
    paginate_by = 12

    def get_queryset(self):
        queryset = Champion.objects.all()

        query = self.request.GET.get("query")
        region = self.request.GET.get("region")
        role = self.request.GET.get("role")

        if query:
            queryset = queryset.filter(
                Q(name__icontains=query)
                | Q(title__icontains=query)
            )

        if region:
            queryset = queryset.filter(region__id=region)

        if role:
            queryset = queryset.filter(roles__id=role)

        return queryset.distinct()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["regions"] = Region.objects.all()
        context["roles"] = Role.objects.all()

        return context


class ChampionDetailView(DetailView):
    model = Champion
    template_name = "catalog/champion_detail.html"


class ChampionCreateView(LoginRequiredMixin, CreateView):
    model = Champion
    form_class = ChampionForm
    template_name = "catalog/champion_form.html"
    success_url = reverse_lazy("champion-list")


class ChampionUpdateView(AdminRequiredMixin, UpdateView):
    model = Champion
    form_class = ChampionForm
    template_name = "catalog/champion_form.html"
    success_url = reverse_lazy("champion-list")


class ChampionDeleteView(AdminRequiredMixin, DeleteView):
    model = Champion
    template_name = "catalog/champion_confirm_delete.html"
    success_url = reverse_lazy("champion-list")


class RegisterView(CreateView):
    form_class = UserRegistrationForm
    template_name = "registration/register.html"
    success_url = reverse_lazy("champion-list")

    def form_valid(self, form):
        response = super().form_valid(form)

        login(
            self.request,
            self.object,
        )

        return response
