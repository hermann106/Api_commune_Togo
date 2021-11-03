from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Region(models.Model):
    name = models.CharField(max_length=100, verbose_name=_("name"))
    description = models.TextField(_("description"), blank=True, null=True)
    coordonate = models.JSONField(blank=True, null=True, verbose_name=_("Coordonate"))
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-created_at"]

class Prefecture(models.Model):
    region = models.ForeignKey(Region, related_name="prefectures", on_delete=models.CASCADE )
    name = models.CharField(max_length=100, verbose_name=_("name"))
    description = models.TextField(_("description"), blank=True, null=True)
    coordonate = models.JSONField(blank=True, null=True, verbose_name=_("Coordonate"))
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-created_at"]

class Commune(models.Model):
    prefecture = models.ForeignKey(Prefecture, related_name="communes", on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name=_("name"))
    description = models.TextField(_("description"), blank=True, null=True)
    coordonate = models.JSONField(blank=True, null=True, verbose_name=_("Coordonate"))
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-created_at"]

class Canton(models.Model):
    commune = models.ForeignKey(Commune, related_name="cantons", on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name=_("name"))
    description = models.TextField(_("description"), blank=True, null=True)
    coordonate = models.JSONField(blank=True, null=True, verbose_name=_("Coordonate"))
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-created_at"]

class Village(models.Model):
    canton = models.ForeignKey(Canton, related_name="villages", on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name=_("name"))
    description = models.TextField(_("description"), blank=True, null=True)
    coordonate = models.JSONField(blank=True, null=True, verbose_name=_("Coordonate"))
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-created_at"]

class Quartier(models.Model):
    name = models.CharField(max_length=100, verbose_name=_("name"))
    description = models.TextField(_("description"), blank=True, null=True)
    coordonate = models.JSONField(blank=True, null=True, verbose_name=_("Coordonate"))
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-created_at"]