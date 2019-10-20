from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    # Our URLS
    path('', TemplateView.as_view(template_name="index.html")),

    # Djoser test stuff
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),

    # Django built in
    path('admin/', admin.site.urls),
]


if settings.DEBUG:
    # Static files for local dev, so we don't have to collectstatic and such
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)

    # Django debug toolbar
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
