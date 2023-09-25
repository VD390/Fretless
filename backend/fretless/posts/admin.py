from django.contrib import admin

from .models import Post, Tag, Follow, Favorite, Comment


class TagAdmin(admin.ModelAdmin):
    ist_display = ('pk', 'username', 'email', 'first_name',
                   'last_name', 'date_of_birth')


admin.site.register(Tag, TagAdmin)
