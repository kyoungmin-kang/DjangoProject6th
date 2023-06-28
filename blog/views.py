from django.conf import settings

from django.shortcuts import render
from django.views.generic import ListView, DetailView, ArchiveIndexView, YearArchiveView, MonthArchiveView, \
    DayArchiveView, TodayArchiveView, TemplateView

from blog.models import Post


# Create your views here.
class PostLV(ListView):
    model = Post
    template_name = 'blog/post_all.html'
    context_object_name = 'posts'
    paginate_by = 2


class PostDV(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        from django.conf import settings
        context['disqus_short'] = f"{settings.DISQUS_SHORTNAME}"
        context['disqus_id'] = f"post-{self.object.id}-{self.object.slug}"
        context['disqus_url'] = f"{settings.DISQUS_DOMAIN}-{self.object.get_absolute_url()}"
        context['disqus_title'] = f"{self.object.slug}"
        return context


class PostAV(ArchiveIndexView):
    model = Post
    date_field = 'modify_dt'


class PostYAV(YearArchiveView):
    model = Post
    date_field = 'modify_dt'
    make_object_list = True
    # month_format = '%b'


class PostMAV(MonthArchiveView):
    model = Post
    date_field = 'modify_dt'
    month_format = '%m'


class PostDAV(DayArchiveView):
    model = Post
    month_format = '%m'
    date_field = 'modify_dt'


class PostTAV(TodayArchiveView):
    model = Post
    date_field = 'modify_dt'
    template_name = 'blog/post_archive_day.html'


class TagCloudTV(TemplateView):
    template_name = 'taggit/taggit cloud.html'


class TaggedObjectLV(ListView):
    template_name = 'taggit/taggit post list.html'
    model = Post

    def get_queryset(self):
        return Post.objects.filter(tags__name=self.kwargs.get('tag'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tagname']= self.kwargs['tag']
        return context
