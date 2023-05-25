from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework import views
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework import routers


urlpatterns = [
    path('admin/', admin.site.urls),
    path('restaurant/', include('restaurant.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

]  + static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS )

