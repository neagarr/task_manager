from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from manager.models import *


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("is_complete", "deadline", "priority", "name", "description")
    list_filter = ("is_complete", "deadline", "priority")
    search_fields = ("name", "description")


@admin.register(TaskType)
class TaskTypeAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Worker)
class WorkerAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("position",)
    fieldsets = UserAdmin.fieldsets + (("Additional Information", {"fields": ("position",)}),)
    add_fieldsets = UserAdmin.add_fieldsets + (("Additional Information", {"fields": (
        "first_name",
        "last_name",
        "position",
    )}),)
