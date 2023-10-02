from django.contrib import admin

from .models import CustomUser


class UserAdmin(admin.ModelAdmin):
    ist_display = ('pk', 'username', 'email', 'first_name',
                   'last_name', 'date_of_birth')


admin.site.register(CustomUser, UserAdmin)
