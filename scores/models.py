from uuid import uuid4

from django.db.models import DateTimeField, IntegerField, Model, UUIDField


class Score(Model):
    score_id = UUIDField(primary_key=True, default=uuid4, editable=False)
    user_id = UUIDField(null=False)
    score = IntegerField(null=False)
    created_at = DateTimeField(auto_now=True, editable=False)
    updated_at = DateTimeField(auto_now_add=True)
