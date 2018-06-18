# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from django.contrib import admin
from Agrus import views


urlpatterns = [
    url(r'^$', views.start, name='start'),
    url(r'^agrus/', include('kurs.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^added/', views.added, name='added'),
    url(r'^register/$', views.RegisterFormView.as_view()),
    url(r'^login/$', views.LoginFormView.as_view()),
    url(r'^logout/$', views.LogoutView.as_view()),
]
