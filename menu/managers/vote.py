from django.db import models
from django.db.models import Count, Sum


class VoteManager(models.Manager):
    def get_score(self, obj):
        result = self.filter(
            object_id=obj._get_pk_val(),
        ).aggregate(score=Sum("vote"), num_votes=Count("vote"))

        if result["score"] is None:
            result["score"] = 0
        return result

    def record_vote(self, obj, user, vote):
        if vote not in (+1, 0, -1):
            raise ValueError("Invalid vote (must be +1/0/-1)")
        try:
            v = self.get(user=user, object_id=obj._get_pk_val())
            if vote == 0:
                v.delete()
            else:
                v.vote = vote
                v.save()
        except models.ObjectDoesNotExist:
            if vote == 0:
                return
            self.create(user=user, object_id=obj._get_pk_val(), vote=vote)
