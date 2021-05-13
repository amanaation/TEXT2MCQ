from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path

from . import views


urlpatterns = [
    path("", views.display_index),
    #path("mydata", views.view_name),
    path("mydata", views.view_name),
]

urlpatterns += staticfiles_urlpatterns()
