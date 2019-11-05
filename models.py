from django.db import models


class User(models.Model):

    name = models.CharField(max_length=255, null=False)

    email = models.EmailField(null=False)

    def __str__(self):
        return "{} - {}".format(self.title, self.artist)