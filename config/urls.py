from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("accounts.urls")),
    path("reviews/", include("reviews.urls")),
    path("search/", include("search.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
