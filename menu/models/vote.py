from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.contrib.auth import get_user_model
from django.utils.timezone import now

from menu.managers import VoteManager


User = get_user_model()

SCORES = (
    (+1, "+1"),
    (-1, "-1"),
)


class Vote(models.Model):
    """
    A vote on an object by a User.
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vote = models.SmallIntegerField(choices=SCORES)
    time_stamp = models.DateTimeField(editable=False, default=now)

    objects = VoteManager()

    class Meta:
        db_table = "votes"

    def __str__(self):
        return f"{self.user}: {self.vote}"

    def is_upvote(self):
        return self.vote == 1

    def is_downvote(self):
        return self.vote == -1
