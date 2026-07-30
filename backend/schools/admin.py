from django.contrib import admin

from .models import House, School, SchoolClass


@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ("name", "phone", "email")


@admin.register(SchoolClass)
class SchoolClassAdmin(admin.ModelAdmin):
    list_display = ("name", "school", "level")
    list_filter = ("school", "level")


@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
    list_display = ("name", "school", "color")
    list_filter = ("school",)