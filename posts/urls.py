from django.conf.urls import url

from .views import (
    post_list,
    post_update,
    post_detail,
    post_create,
    post_delete
)

# urlpatterns = [
#     url(r'^$', posts_list, name='list'),
#     url(r'^create/$', posts_create),
#     url(r'^(?P<slug>\d+)/$', posts_detail, name='detail'),
#     url(r'^(?P<slug>\d+)/edit$', posts_update, name='update'),
#     url(r'^(?P<slug>\d+)/delete/$', posts_delete)
# ]

urlpatterns = [
    url(r'^$', post_list, name='list'),
    url(r'^create/$', post_create),
    url(r'^(?P<slug>[\w-]+)/$', post_detail, name='detail'),
    url(r'^(?P<slug>[\w-]+)/edit/$', post_update, name='update'),
    url(r'^(?P<slug>[\w-]+)/delete/$', post_delete),
    # url(r'^posts/$', "<appname>.views.<function_name>"),
]
