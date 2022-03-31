from rest_framework.viewsets import ModelViewSet

from scores.models import Score
from scores.serializers import UserSerializer


class ScoreViewSet(ModelViewSet):
    class META:
        lookup_field = 'score_id'

    queryset = Score.objects.all()
    serializer_class = UserSerializer
