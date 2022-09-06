from django.contrib import admin

# Register your models here.
from firstapp.models import Vehicle
class VehicleAdmin(admin.ModelAdmin):
    list_display = ['vehicle_number' ,'vehicle_type' ,'vehicle_model' , 'vehicle_description']


admin.site.register(Vehicle ,VehicleAdmin)
