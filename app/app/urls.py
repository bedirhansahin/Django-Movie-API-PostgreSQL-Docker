from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    # Rest Framework's login and logout views.
    path('api-auth/', include('rest_framework.urls')),
    # API
    path('api/', include('movie.api.urls')),
    path('api/', include('core.api.urls')),
    # Swagger Documentation
    path('api/schema', SpectacularAPIView.as_view(), name='api-schema'),
    path('api/docs', SpectacularSwaggerView.as_view(url_name='api-schema'), name='api-docs'),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )
