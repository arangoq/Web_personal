from django.contrib import admin
from .models import Interest


class InterestAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Interest, InterestAdmin)
