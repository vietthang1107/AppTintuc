from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from rest_framework.permissions import AllowAny
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(title='App Online API', default_version='v1'),
    url=settings.SWAGGER_URL,
    public=True,
    permission_classes=(AllowAny,),
)

urlpatterns = \
    [
        # path('admin/', admin.site.urls),
        path('', include('news.urls')),
    ]

if settings.SHOW_API_DOC:
    urlpatterns += [
        path('docs/', schema_view.with_ui('swagger', cache_timeout=0)),
        # path('redocs/', schema_view.with_ui('redoc', cache_timeout=0))
    ]
