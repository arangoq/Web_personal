from django.contrib import admin
from .models import Skills


class SkillsAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Skills, SkillsAdmin)
