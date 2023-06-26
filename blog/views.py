from django.shortcuts import render
from django.views.generic import ListView, ArchiveIndexView, DetailView

from blog.models import Post


# Create your views here.
class PostLV(ListView):
    model = Post
    template_name = 'blog/post_all.html'
    context_object_name = 'posts'
    paginate_by = 2

class PostDV(DetailView):
    model = Post


class PostAV(ArchiveIndexView):
    model = Post
    date_field = 'modify_dt'


class YearArchiveIndexView:
    pass


class PostYAV(YearArchiveIndexView):
    model = Post
    date_field = 'modify_dt'
    make_object_list = True
    # month_format = '%b'


class MonthArchiveIndexView:
    pass


class PostMAV(MonthArchiveIndexView):
    model = Post
    date_field = 'modify_dt'


class DayArchiveIndexView:
    pass


class PostDAV(DayArchiveIndexView):
    model = Post
    date_field = 'modify_dt'


class TodayArchiveIndexView:
    pass


class PostTAV(TodayArchiveIndexView):
    model = Post
    date_field = 'modify_dt'