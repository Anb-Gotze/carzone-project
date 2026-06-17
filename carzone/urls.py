from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),
    path('cars/', include('cars.urls')),
    path('account/', include('accounts.urls')),
    path('socialaccount/', include('allauth.urls')),
    path('contacts/', include('contacts.urls')),
]

# This forces Django to serve media and static files even when DEBUG is False on Render
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)