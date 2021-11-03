from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Composition(models.Model):
    name = models.CharField(max_length=100, verbose_name=_("name"))
    agglomeration = models.CharField(max_length=100, verbose_name=_("name"), help_text=_("Canton or Quartier"))
    description = models.TextField(_("description"), blank=True, null=True)
    coordonate = models.JSONField(blank=True, null=True, verbose_name=_("Coordonate"))
    prefecture = models.CharField(max_length=100, verbose_name=_("prefecture"))
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-created_at"]