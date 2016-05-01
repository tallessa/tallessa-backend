# encoding: utf-8

from django.db import models


class Tenant(models.Model):
    slug = models.SlugField(unique=True)
    name = models.CharField(max_length=255)

    # admin_group = models.ForeignKey('auth.Group', related_name='as_admin_group_for_tenants')
    # user_group = models.ForeignKey('auth.Group', related_name='as_user_group_for_tenants')
