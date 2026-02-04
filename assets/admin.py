from django.contrib import admin
from .models import Asset


@admin.register(Asset)
class AssetAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "asset_name",
        "asset_type",
        "quantity",
        "purchase_price",
        "created_at",
    )

    list_filter = ("asset_type",)
    search_fields = ("asset_name", "user__username")
