from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Commune(models.Model):
    name = models.CharField(max_length=100, verbose_name=_("name"))
    description = models.TextField(_("description"), blank=True, null=True)
    cordonate = models.JSONField(blank=True, null=True)
    region = models.CharField(max_length=100, verbose_name=_("name"))
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-created_at"]

