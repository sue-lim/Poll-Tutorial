from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path(
        "polls/", include("polls.urls")
    ),  # linking here from polls url & will take you to the page
    path("admin/", admin.site.urls),  # link to the /admin page
]
