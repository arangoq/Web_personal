from django.contrib import admin
from .models import Awards


class AwardsAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Awards, AwardsAdmin)
