from django.contrib import admin
from .models import Staff
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class StaffResource(resources.ModelResource):
    class Meta:
        model = Staff

class StaffAdmin(ImportExportModelAdmin):
    resource_class = StaffResource

admin.site.register(Staff,StaffAdmin)

