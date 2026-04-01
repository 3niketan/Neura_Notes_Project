from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("user_auth.urls")),
    path("", include("NeuraNotes.urls")),
]
