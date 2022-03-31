from uuid import uuid4

from django.db.models import CharField, DateTimeField, Model, UUIDField


class User(Model):
    class Meta:
        # managed = False
        db_table = "Users"

    user_id = UUIDField(primary_key=True, default=uuid4, editable=False)
    name = CharField(max_length=60, null=False)
    created_at = DateTimeField(auto_now=True, editable=False)
    updated_at = DateTimeField(auto_now_add=True)
