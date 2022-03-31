from rest_framework.viewsets import ModelViewSet

from models import Score
from serializers import UserSerializer


class UserViewSet(ModelViewSet):
    queryset = Score.objects.all()
    serializer = UserSerializer(queryset, many=True)
