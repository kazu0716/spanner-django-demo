from rest_framework.serializers import ModelSerializer

from models import Score


class UserSerializer(ModelSerializer):
    class Meta:
        model = Score
        fields = ['user_id', 'score']
