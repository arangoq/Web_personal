from django.contrib import admin
from .models import Experience


class ExperienceAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Experience, ExperienceAdmin)
