from django.contrib import admin


from .models import Event, EventLike


class EventAdmin(admin.ModelAdmin):
    list_display = ("name", "location", "url", "start_date", "end_date", "likes")
    list_filter = ("start_date", "end_date")
    search_fields = ("name", "location")


admin.site.register(Event, EventAdmin)


class EventLikeAdmin(admin.ModelAdmin):
    list_display = ("event", "user", "liked_at", "attending")
    list_filter = ("liked_at", "attending")
    search_fields = ("event__name", "user")

    def event(self, obj):
        return obj.event.name


admin.site.register(EventLike, EventLikeAdmin)
