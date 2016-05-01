# encoding: utf-8

from django.db import models


class Tenant(models.Model):
    slug = models.SlugField(unique=True)
    name = models.CharField(max_length=255)
    hostname = models.CharField(max_length=511)

    # admin_group = models.ForeignKey('auth.Group', related_name='as_admin_group_for_tenants')
    # user_group = models.ForeignKey('auth.Group', related_name='as_user_group_for_tenants')

    @property
    def tenant(self):
        return self

    def __str__(self):
        return self.slug

    def save(self, *args, **kwargs):
        if self.slug and not self.hostname:
            self.hostname = '{slug}.{hostname_suffix}'.format(
                slug=self.slug,
                hostname_suffix=settings.TALLESSA_HOSTNAME_SUFFIX,
            )

        return super(Tenant, self).save(*args, **kwargs)
