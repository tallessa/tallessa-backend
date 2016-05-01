from django.db import models
from django.utils.translation import ugettext_lazy as _


class Item(models.Model):
    tenant = models.ForeignKey('tallessa_tenants.Tenant', related_name='stuff')
    slug = models.SlugField()

    name = models.CharField(max_length=255)
    # model = models.ForeignKey('tallessa_stuff.Model')
    serial_number = models.CharField(max_length=255, blank=True)

    home_location = models.ForeignKey(
        'tallessa_stuff.Location',
        blank=True,
        null=True,
        related_name='as_current_location_for_items',
    )

    current_location = models.ForeignKey(
        'tallessa_stuff.Location',
        blank=True,
        null=True,
    )

    parent = models.ForeignKey('self', blank=True, null=True, related_name='contents')

    class Meta:
        verbose_name = _('item')
        verbose_name_plural = _('stuff')
        unique_together = [('tenant', 'slug')]
        index_together = [('tenant', 'serial_number')]

    def __str__(self):
        return self.slug
