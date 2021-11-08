from django.contrib import admin
from .models import Commune,Prefecture,Canton,Quartier,Region,Village
# Register your models here.

class CommuneInline(admin.TabularInline):
    model = Commune

class CantonInline(admin.TabularInline):
    model = Canton

@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']

@admin.register(Prefecture)
class PrefectureAdmin(admin.ModelAdmin):
    list_display = ['region','name', 'description']
    inlines = [CommuneInline]



@admin.register(Commune)
class CommuneAdmin(admin.ModelAdmin):
    list_display = ['prefecture','name', 'description']
    inlines = [CantonInline]

@admin.register(Canton)
class CantonAdmin(admin.ModelAdmin):
    list_display = ['commune','name', 'description']

@admin.register(Village)
class VillageAdmin(admin.ModelAdmin):
    list_display = ['canton','name', 'description']

@admin.register(Quartier)
class QuartierAdmin(admin.ModelAdmin):
    list_display = ['village','name', 'description']