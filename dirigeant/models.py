from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Leader(models.Model):
    name = models.CharField(max_length=100, verbose_name=_("name"))
    fonction = models.CharField(max_length=100, verbose_name=_("fonction"))
    description = models.TextField(_("description"), blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-created_at"]