from django.contrib import admin
from violation.models import Violation


@admin.register(Violation)
class TemplateCategoryAdmin(admin.ModelAdmin):
    list_display = ('image', 'time', 'place', 'is_active', 'description', 'created_at', 'updated_at',)
    search_fields = ('description',)
    readonly_fields = ('created_at', 'updated_at')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()