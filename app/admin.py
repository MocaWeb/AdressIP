from django.contrib import admin
from .models import Category, Link
# Register your models here.
from import_export.admin import ImportExportModelAdmin
from rangefilter.filters import DateRangeFilter
class LinkAdmin(admin.ModelAdmin):

    list_filter = ('url','is_active',)

class CategoryAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ('name','device_type','browser_type','location_country','location_city',)
    list_filter = (   ('timestamp', DateRangeFilter),'location_country')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Link, LinkAdmin)