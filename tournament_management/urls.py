"""
URL configuration for tournament_management project.

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

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
]
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import (
    TournamentViewSet, TeamViewSet, FixtureViewSet,
    CustomAuthToken, RegisterView, LogoutView, create_team
)

router = DefaultRouter()
router.register(r'tournaments', TournamentViewSet)
router.register(r'teams', TeamViewSet)
router.register(r'fixtures', FixtureViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-token-auth/', CustomAuthToken.as_view(), name='api-token-auth'),
    path('register/', RegisterView.as_view(), name='register'),  # Registration endpoint
    path('logout/', LogoutView.as_view(), name='logout'),  # Logout endpoint
    path('create-team/', create_team, name='create_team'),
    path('', include(router.urls)),
]