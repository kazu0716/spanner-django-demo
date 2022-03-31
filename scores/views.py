from rest_framework.viewsets import ModelViewSet

from scores.models import Score
from scores.serializers import UserSerializer


class ScoreViewSet(ModelViewSet):
    queryset = Score.objects.all()
    serializer = UserSerializer(queryset, many=True)
