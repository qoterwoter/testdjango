from django.urls import path
from . import views
from django.conf.urls import include, url
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('users',UserViewSet)
urlpatterns = [
    path('', views.index, name='main'),
    path('about', views.about, name='about'),
    path('landing', views.landing, name='landing'),
    url(r'^drivers/$', views.drivers_list),
    url(r'^drivers/(?P<id>[0-9]+)$', views.drivers_detail),
    url(r'^news/$',views.news_list),
    path('news/', views.news_list, name='news'),
    path('drivers/', views.drivers_list, name='drivers'),
    # path('users/', views.UserView.as_view(),name='users'),
    path ('',include(router.urls))
]
