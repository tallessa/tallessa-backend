from django.db import models


class Location(models.Model):
    tenant = models.ForeignKey('tallessa_tenants.Tenant', related_name='locations')
    slug = models.SlugField()
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.slug
