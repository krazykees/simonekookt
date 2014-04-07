from django.conf.urls import patterns, url
from django.views.generic import ListView, DetailView
from blogengine.models import Category, Post, Tag
from blogengine.views import CategoryListView, TagListView

urlpatterns = patterns('',
    # Index
    url('^(?P<page>\d+)?/?$', ListView.as_view(
        model=Post,
        paginate_by=5,
        )),

    # Individual posts
    url(r'^(?P<pub_date__year>\d{4})/(?P<pub_date__month>\d{1,2})/(?P<slug>[a-zA-Z0-9-]+)/?$', DetailView.as_view(
        model=Post,
        )),

    # Categories
    url(r'^category/(?P<slug>[a-zA-z0-9-]+)/?$', CategoryListView.as_view(
        paginate_by=5,
        model=Category,
    )),

    url(r'^tag.(?P<slug>[a-zA-z0-9-]+)/?$', TagListView.as_view(
        paginate_by=5,
        model=Tag,
    ))
)