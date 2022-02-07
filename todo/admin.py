from django.contrib import admin
from .models import Todo


class TodoAdmin(admin.ModelAdmin):
    readonly_fields = ('date_create',)


admin.site.register(Todo, TodoAdmin)
