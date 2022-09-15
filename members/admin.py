from django.contrib import admin
from .models import Members

class MembersAdmin(admin.ModelAdmin):
    list_display = ('firstname','lastname')


admin.site.register(Members,MembersAdmin)
# Register your models here.
