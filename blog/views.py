from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, ArchiveIndexView, YearArchiveView, MonthArchiveView, \
    DayArchiveView, TodayArchiveView, TemplateView, FormView, CreateView, UpdateView, DeleteView

from mysite.views import OwnerOnlyMixin

class PostCreateView(LoginRequiredMixin, CreateView):
    pass


class PostChangeLV(LoginRequiredMixin, ListView):
    pass


class PostUpdateView(OwnerOnlyMixin, UpdateView):
    pass


class PostDeleteView(OwnerOnlyMixin, DeleteView):
    pass