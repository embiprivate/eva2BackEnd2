from django.contrib import admin

# Register your models here.
# Register your models here.
from tiendaApp.models import Producto
from tiendaApp.models import Cargo,Departamento,Empleado,Usuario

class ProductoAdmin(admin.ModelAdmin):
    #list_display es lo que yo quiero que se vea en la tabla
    list_display = ['numProducto','nombreProducto']

admin.site.register(Producto,ProductoAdmin)



# EMPLEADOS

class CargoAdmin(admin.ModelAdmin):
    list_display = ['id','nombre']

class DepartamentoAdmin(admin.ModelAdmin):
    list_display = ['codigo','nombre']

class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ['run','nombre','paterno','materno',
                    'codigoEmpleado','sueldo','cargo',
                    'departamento']
    
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ['run','nombres','apellidos','sexo','fechaNac',
                    'email','contras','repcontras']

admin.site.register(Cargo,CargoAdmin)
admin.site.register(Departamento,DepartamentoAdmin)
admin.site.register(Empleado,EmpleadoAdmin)
admin.site.register(Usuario,UsuarioAdmin)