from django.contrib import admin

from .models import User


class NinjaAdmin(admin.ModelAdmin):
    pass


admin.site.register(User, NinjaAdmin)
