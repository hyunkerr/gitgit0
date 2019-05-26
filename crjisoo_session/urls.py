"""crjisoo_session URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.index, name='index')
Class-based views
    1. Add an import:  from other_app.views import index
    2. Add a URL to urlpatterns:  url(r'^$', index.as_view(), name='index')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin
from blog import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name = "index"),
    url(r'^new/$', views.new, name = "new"),
    url(r'^post/(?P<index>\d+)$',views.post_detail, name="post_detail"),
    url(r'^post/(?P<index>\d+)/edit/$',views.post_edit, name="post_edit"),
    url(r'^post/(?P<index>\d+)/delete/$',views.post_delete, name="post_delete"),
]
