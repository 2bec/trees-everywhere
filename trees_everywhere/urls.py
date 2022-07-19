from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from api import urls as api_urls

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("accounts.urls")),
    path("trees/", include("trees.urls")),
    path("users/", include("users.urls")),
    path("api/", include(api_urls)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
