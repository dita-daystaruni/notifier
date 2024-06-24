from django.contrib import admin

from .models import Organization


class OrganizationAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    list_display = ("id", "name", "phone", "email", "date_added")


# Register your models here.
admin.site.register(Organization, OrganizationAdmin)
