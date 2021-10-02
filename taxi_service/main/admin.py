from django.contrib import admin
from .models import *
from django.db.models.functions import Lower
from import_export.admin import ImportExportModelAdmin
from import_export.formats import base_formats
@admin.register(News)
class NewsAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ("id","title","description","date",'user')
    search_fields = ['title','description']
    list_filter = ['user','date']
    pass
    def get_orering(self,request):
          return [Lower('id')]
@admin.register(Drivers)
class DriversAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ("id","name","surname","rating")
    search_fields = ['name','surname']
    list_filter = ['rating']
    pass
    def get_ordering(self, request):
        return [Lower('id')]
    def get_import_formats(self):
            formats = (
                  base_formats.XLS,
                  base_formats.XLSX,
            )
            return [f for f in formats if f().can_import()]
    def get_export_formats(self):
            formats = (
                  base_formats.XLS,
                  base_formats.XLSX,
            )
            return [f for f in formats if f().can_export()]

@admin.register(DriversPhoto)
class DriversPhotoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('driver_id',"photo_id","url")
    search_fields = ['driver_id']
    list_filter = ['driver_id']
    pass
    def get_ordering(self, request):
        return [Lower('photo_id')]
    def get_import_formats(self):
            formats = (
                  base_formats.XLS,
                  base_formats.XLSX,
            )
            return [f for f in formats if f().can_import()]
    def get_export_formats(self):
            formats = (
                  base_formats.XLS,
                  base_formats.XLSX,
            )
            return [f for f in formats if f().can_export()]

@admin.register(Cars)
class CarsAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ("mark","model")
    search_fields = ['mark','model']
    list_filter = ['mark','model']
    pass
    def get_ordering(self, request):
        return [Lower('mark')]
    def get_import_formats(self):
            formats = (
                  base_formats.XLS,
                  base_formats.XLSX,
            )
            return [f for f in formats if f().can_import()]
    def get_export_formats(self):
            formats = (
                  base_formats.XLS,
                  base_formats.XLSX,
            )
            return [f for f in formats if f().can_export()]

@admin.register(DriversCars)
class DriversCarsAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ("id","car_id","driver_id")
    list_filter = ['driver_id', "car_id"]
    search_fields = ['driver_id__name','driver_id__surname','car_id__name']
    pass
    def get_ordering(self, request):
        return [Lower('id')]
    def get_import_formats(self):
            formats = (
                  base_formats.XLS,
                  base_formats.XLSX,
            )
            return [f for f in formats if f().can_import()]
    def get_export_formats(self):
            formats = (
                  base_formats.XLS,
                  base_formats.XLSX,
            )
            return [f for f in formats if f().can_export()]

@admin.register(Clients)
class ClientsAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ("id", "name", "rating")
    list_filter = ['name']
    search_fields = ['name','rating']
    pass
    def get_ordering(self, request):
        return [Lower('id')]
    def get_import_formats(self):
            formats = (
                  base_formats.XLS,
                  base_formats.XLSX,
            )
            return [f for f in formats if f().can_import()]
    def get_export_formats(self):
            formats = (
                  base_formats.XLS,
                  base_formats.XLSX,
            )
            return [f for f in formats if f().can_export()]