from django.contrib import admin
from . models import Core


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',),}
admin.site.register(Core,PostAdmin)