from rest_framework import viewsets, permissions
from rest_framework.authtoken.views import ObtainAuthToken
from .models import Tournament, Team, Fixture
from .serializers import TournamentSerializer, TeamSerializer, FixtureSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from django.contrib.auth import logout


class TournamentViewSet(viewsets.ModelViewSet):
    queryset = Tournament.objects.all()
    serializer_class = TournamentSerializer
    permission_classes = [permissions.IsAuthenticated]


class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    permission_classes = [permissions.IsAuthenticated]


class FixtureViewSet(viewsets.ModelViewSet):
    queryset = Fixture.objects.all()
    serializer_class = FixtureSerializer
    permission_classes = [permissions.IsAuthenticated]


class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        return Response({'token': token.key, 'user_id': token.user_id, 'email': token.user.email})


class RegisterView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        User = get_user_model()
        user = User.objects.create_user(username=username, password=password)
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key}, status=status.HTTP_201_CREATED)


class LogoutView(APIView):
    def post(self, request):
        request.user.auth_token.delete()
        logout(request)
        return Response(status=status.HTTP_200_OK)
