"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from Share.views import HomeView,delete_file,DisplayView,DisplayView_detail,SearchView,MyView
"""
app_name="Share";
"""
urlpatterns = [
    # url(r'^admin/', include(admin.site.urls)),
    # path('admin/', admin.site.urls),
    url(r'^$',HomeView.as_view(),name="home"),
    url(r'^detail/(?P<code>\d+)/$',DisplayView_detail.as_view(),name="detail"),
    url(r'^s/(?P<code>\d+)/$',DisplayView.as_view(),name="detail_code"),
    url(r'^search/',SearchView.as_view(),name="search"),
    url(r'^my/$',MyView.as_view(),name="MY"),
    url(r'^delete_file/(?P<code>\d+)/$',delete_file.as_view(),name="delete_file")

]
