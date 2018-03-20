from django.conf.urls import url
from contact import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view(), name='index'),
    url(r'^list/$', views.ListPageView.as_view(), name='list'),
    url(r'^add/$', views.AddPageView.as_view(), name='add'),
    url(r'^about/$', views.AboutPageView.as_view(), name='about'),
]