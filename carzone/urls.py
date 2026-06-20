from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponse
from django.contrib.auth.models import User

# --- TEMPORARY EMERGENCY CREATOR ---
def create_emergency_admin(request):
    username = "abakwume"
    email = "abakwumegodwin1@gmail.com"
    password = "CarzoneLive2026"
    
    if not User.objects.filter(username=username).exists():
        User.objects.create_superuser(username, email, password)
        return HttpResponse(f"<h1>Success! Account created.</h1><p>Username: {username}</p>")
    else:
        # If the user exists but the password was wrong/broken, this will overwrite it and fix it!
        user = User.objects.get(username=username)
        user.set_password(password)
        user.save()
        return HttpResponse(f"<h1>Success! Password reset for existing user: {username}</h1>")
# -----------------------------------

urlpatterns = [
    path('setup-admin-key/', create_emergency_admin), # <-- Keep this line here
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),
    path('cars/', include('cars.urls')),
    path('accounts/', include('accounts.urls')),
    path('contacts/', include('contacts.urls')),
]

# This forces Django to serve media and static files even when DEBUG is False on Render
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
