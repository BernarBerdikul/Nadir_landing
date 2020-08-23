from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('supersecretadmin/', admin.site.urls),
    path('', include('landing_page.urls'))
] + static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS) \
  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
