from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from store import settings

urlpatterns = [
    path('admin/', admin.site.urls),  
    path('', include('products.urls')),
    path('users/', include('users.urls'))
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)