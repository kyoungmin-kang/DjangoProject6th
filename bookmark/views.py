from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from mysite.views import OwnerOnlyMixin

# 중략

class BookmarkCreateView(LoginRequiredMixin, CreateView):
    pass

class BookmarkChangeLV(LoginRequiredMixin, ListView):
    pass

class BookmarkUpdateView(OwnerOnlyMixin, UpdateView):
    pass

class BookmarkDeleteView(OwnerOnlyMixin, DeleteView):
    pass