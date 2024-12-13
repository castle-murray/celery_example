from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    # re_path(r'^startAPSchedulerCode/$', views.startAPSchedulerCode, name='startAPSchedulerCode'),
    re_path(r'^runAPS/$', views.runAPS, name='runAPS'),
    re_path(r'^tick/$', views.tick, name='tick'),
]
