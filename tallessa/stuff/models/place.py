from django.db import models


class Place(models.Model):
    team = models.ForeignKey('tallessa_teams.Team', related_name='places')
    slug = models.SlugField()
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.slug
