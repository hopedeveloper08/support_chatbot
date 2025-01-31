from django.contrib import admin

from .models import Bussiness

@admin.register(Bussiness)
class BussinessAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    