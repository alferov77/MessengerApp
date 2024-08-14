"""
URL configuration for messenger_p project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from chat.views import ChatGroupViewSet, MessageViewSet, home_view, profile_view, users_view, chatgroups_view
from django.conf import settings
from django.conf.urls.static import static

router = DefaultRouter()
router.register(r'chatgroups', ChatGroupViewSet)
router.register(r'messages', MessageViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('', home_view, name='home'),
    path('profile/', profile_view, name='profile'),
    path('users/', users_view, name='users'),
    path('chatgroups/', chatgroups_view, name='chatgroups'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('chat/', include('chat.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)










