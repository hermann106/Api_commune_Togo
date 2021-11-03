from django.contrib import admin
from .models import Commune,Prefecture,Canton,Quartier,Region,Village
# Register your models here.

@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    pass

@admin.register(Prefecture)
class PrefectureAdmin(admin.ModelAdmin):
    pass

@admin.register(Commune)
class CommuneAdmin(admin.ModelAdmin):
    pass

@admin.register(Canton)
class CantonAdmin(admin.ModelAdmin):
    pass

@admin.register(Village)
class VillageAdmin(admin.ModelAdmin):
    pass

@admin.register(Quartier)
class QuartierAdmin(admin.ModelAdmin):
    pass