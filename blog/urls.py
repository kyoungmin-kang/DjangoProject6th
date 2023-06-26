from django.urls import path, re_path

from blog import views

app_name = 'blog'
urlpatterns = [
    path('', views.PostLV.as_view(), name='index'),
    path('post/', views.PostLV.as_view(), name='post_list'),

    re_path(r'^post/(?P<slug>[-\w]+)/$', views.PostDV.as_view(), name='post_detail'), #레귤러 익스프레션 (정규 표현식)<- chat gpt 가 만들어줌

    path('archive/', views.PostAV.as_view(), name='post_archive'),

    path('archive/<int:year>/', views.PostYAV.as_view(), name='post_year_archive'),

    path('archive/<int:year>/<int:month>/', views.PostMAV.as_view(), name='post_month_archive'),

    path('archive/<int:year>/<int:month>/<int:day>/', views.PostDAV.as_view(), name='post_day_archive'),

    path('archive/today/', views.PostTAV.as_view(), name='post_today_archive'),
]