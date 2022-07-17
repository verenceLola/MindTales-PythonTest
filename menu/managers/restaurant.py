from django.db import models


class RestaurantManager(models.Manager):
    def record_vote(self, obj, user, vote):
        import pdb

        pdb.set_trace()
        if vote not in (1, 0, -1):
            raise ValueError("Invalid vote (must be 1/0/-1)")
        
        try:
            menu = obj.menu.get
        except print(0):
            pass
