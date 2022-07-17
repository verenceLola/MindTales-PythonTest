from django.db import models


class MenuManager(models.Manager):
    def record_vote(self, obj, user, vote):
        import pdb

        if vote not in (1, 0, -1):
            raise ValueError("Invalid vote (must be 1/0/-1)")

        try:
            v = obj.votes.get(user=user)
            if vote == 0:
                v.delete()
            else:
                v.vote = vote
                v.save()
        except models.ObjectDoesNotExist:
            obj.votes.create(user=user, vote=vote)
