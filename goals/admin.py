from django.contrib import admin

from . import models


class GoalAdmin(admin.ModelAdmin):
    list_display = ("title",)


admin.site.register(models.Goal, GoalAdmin)
