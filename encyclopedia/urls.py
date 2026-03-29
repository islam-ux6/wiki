from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.show_ent, name="show_ent"),
    path("search", views.search, name="search"),
    path("create", views.create, name="create"),
    path("edit/<str:name>", views.edit, name="edit"),
    path("random", views.random, name="random")
]
