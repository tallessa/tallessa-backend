# encoding: utf-8

from django.conf import settings
from django.db import models

from tallessa.utils import slugify


class Team(models.Model):
    slug = models.SlugField(unique=True)
    name = models.CharField(max_length=255)
    hostname = models.CharField(max_length=511, unique=True)

    admin_group = models.ForeignKey('auth.Group', related_name='as_admin_group_for_teams')
    user_group = models.ForeignKey('auth.Group', related_name='as_user_group_for_teams')

    @property
    def team(self):
        return self

    def __str__(self):
        return self.slug

    def get_or_create_group(self, suffix):
        from django.contrib.auth.models import Group

        assert self.slug

        return Group.objects.get_or_create(name='{installation_slug}-{team_slug}-{suffix}'.format(
            installation_slug=settings.TALLESSA_INSTALLATION_SLUG,
            team_slug=self.slug,
            suffix=suffix,
        ))

    def save(self, *args, **kwargs):
        if self.name and not self.slug:
            # TODO handle too long and duplicate slugs
            self.name = slugify(self.name)

        if self.slug and not self.hostname:
            self.hostname = '{slug}.{hostname_suffix}'.format(
                slug=self.slug,
                hostname_suffix=settings.TALLESSA_HOSTNAME_SUFFIX,
            )

        if self.admin_group_id is None and self.slug:
            self.admin_group, unused = self.get_or_create_group('admins')
        if self.user_group_id is None and self.slug:
            self.user_group, unused = self.get_or_create_group('users')

        return super(Team, self).save(*args, **kwargs)
