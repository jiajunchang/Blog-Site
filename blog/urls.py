from django.urls import path
from . import views

app_name = "blog"
urlpatterns = [
    # post views
    path("", views.get_post_list, name = "get_post_list"),
    path(
        "<int:year>/<int:month>/<int:day>/<str:slug>",
        views.get_single_post,
        name = "get_single_post"
    )
]