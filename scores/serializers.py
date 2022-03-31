from rest_framework.serializers import ModelSerializer

from scores.models import Score


class UserSerializer(ModelSerializer):
    class Meta:
        model = Score
        fields = ['user_id', 'score']
