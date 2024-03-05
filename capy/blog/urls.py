from django.urls import path

from . import views

urlpatterns = [
    path("", views.loupak),
    path("eminem", views.post_list, name="postlist"),
]