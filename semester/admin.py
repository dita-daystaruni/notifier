from django.contrib import admin
from .models import Semester, SemesterEvent

# Register your models here.


class SemesterAdmin(admin.ModelAdmin):
    list_display = ("name", "code", "start_date", "end_date")
    list_filter = ("start_date", "end_date")
    search_fields = ("name", "location")


admin.site.register(Semester, SemesterAdmin)


class SemesterEventAdmin(admin.ModelAdmin):
    list_display = ("semester", "name", "start_date", "end_date")
    list_filter = ("semester",)

    def event(self, obj):
        return obj.event.name


admin.site.register(SemesterEvent, SemesterEventAdmin)
