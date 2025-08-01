from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.views.generic.base import RedirectView


urlpatterns = [
    path('', RedirectView.as_view(url='/ru/', permanent=True)),
    path('i18n/', include('django.conf.urls.i18n')),
]


urlpatterns += i18n_patterns(
    path('', include('main.urls')),
    path('mentors/', include('mentors.urls')),
    path('events/', include('events.urls')),
    path('partners/', include('partners.urls')),
    path('admin/', admin.site.urls),

    prefix_default_language=True,
)



if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



