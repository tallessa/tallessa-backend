from django.contrib.auth import get_user_model
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated

from .filters import UserTeamFilterBackend
from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    lookup_field = 'username'
    queryset = get_user_model().objects.all()
    filter_backends = (UserTeamFilterBackend,)
    serializer_class = UserSerializer


class CurrentUserView(generics.RetrieveUpdateDestroyAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.user
