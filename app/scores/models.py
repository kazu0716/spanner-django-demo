from django.db.models import DateTimeField, IntegerField, Model, UUIDField


class Score(Model):
    class Meta:
        managed = False
        db_table = "Scores"
        unique_together = (('user_id', 'score_id'), ('user_id', 'score_id'),)

    score_id = UUIDField(auto=True, primary_key=True, editable=False)
    user_id = UUIDField(primary_key=True, editable=False)
    score = IntegerField(null=False)
    created_at = DateTimeField(auto_now=True, editable=False)
    updated_at = DateTimeField(auto_now_add=True)
