from django.contrib import admin
from interview.inventory.models import InventoryTag, InventoryLanguage, InventoryType, Inventory

class InventoryTagAdmin(admin.ModelAdmin):
    """
    InventoryTag admin
    """


class InventoryLanguageAdmin(admin.ModelAdmin):
    """
    InventoryLanguage admin
    """


class InventoryTypeAdmin(admin.ModelAdmin):
    """
    InventoryType admin
    """


class InventoryAdmin(admin.ModelAdmin):
    """
    Inventory admin
    """
    list_display = ('name', 'type', 'language', 'created_at', 'updated_at')
    search_fields = ('name', 'type__name', 'language__name')
    list_filter = ('type', 'language')
    filter_horizontal = ('tags',)


admin.site.register(InventoryTag, InventoryTagAdmin)
admin.site.register(InventoryLanguage, InventoryLanguageAdmin)
admin.site.register(InventoryType, InventoryTypeAdmin)
admin.site.register(Inventory, InventoryAdmin)
