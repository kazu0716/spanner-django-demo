from rest_framework.viewsets import ModelViewSet

from users.models import User
from users.serializers import UserSerializer


class UserViewSet(ModelViewSet):
    class META:
        lookup_field = 'user_id'

    queryset = User.objects.all()
    serializer_class = UserSerializer
