from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import (SpectacularAPIView, SpectacularRedocView,
                                   SpectacularSwaggerView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("core.urls"))
]

if settings.DEBUG:
    urlpatterns += [
        path("schema", SpectacularAPIView.as_view(), name="schema"),
        path("swagger", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
        path("redoc", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
    ]
