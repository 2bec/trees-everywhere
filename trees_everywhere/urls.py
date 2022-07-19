from django.contrib import admin
from django.urls import path, include, reverse_lazy
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

from api import urls as api_urls

urlpatterns = [
    path("", RedirectView.as_view(url=reverse_lazy("login"), permanent=False)),
    path("admin/", admin.site.urls),
    path("accounts/", include("accounts.urls")),
    path("trees/", include("trees.urls")),
    path("users/", include("users.urls")),
    path("api/", include(api_urls)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
