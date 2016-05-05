# encoding: utf-8

from django.conf import settings
from django.db import models


class Team(models.Model):
    slug = models.SlugField(unique=True)
    name = models.CharField(max_length=255)
    hostname = models.CharField(max_length=511, unique=True)

    # admin_group = models.ForeignKey('auth.Group', related_name='as_admin_group_for_teams')
    # user_group = models.ForeignKey('auth.Group', related_name='as_user_group_for_teams')

    @property
    def team(self):
        return self

    def __str__(self):
        return self.slug

    def save(self, *args, **kwargs):
        if self.slug and not self.hostname:
            self.hostname = '{slug}.{hostname_suffix}'.format(
                slug=self.slug,
                hostname_suffix=settings.TALLESSA_HOSTNAME_SUFFIX,
            )

        return super(Team, self).save(*args, **kwargs)
