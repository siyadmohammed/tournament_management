# from django.contrib import admin
# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from .views import (
#     TournamentViewSet, TeamViewSet, FixtureViewSet,
#     CustomAuthToken, RegisterView, LogoutView
# )
#
# router = DefaultRouter()
# router.register(r'tournaments', TournamentViewSet)
# router.register(r'teams', TeamViewSet)
# router.register(r'fixtures', FixtureViewSet)
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('api-token-auth/', CustomAuthToken.as_view(), name='api-token-auth'),
#     path('register/', RegisterView.as_view(), name='register'),  # Registration endpoint
#     path('logout/', LogoutView.as_view(), name='logout'),  # Logout endpoint
#     path('', include(router.urls)),
# ]