from django.contrib import admin

from stories.models import Story


# Register your models here.
class StoryAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "organization",
        "text",
        "date_added",
        "date_of_expiry",
        "hex_code",
    )


admin.site.register(Story, StoryAdmin)
