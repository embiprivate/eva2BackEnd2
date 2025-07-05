from django.db import models
from django.utils import timezone
import os
from tiendaApp.choices import sexos
# Create your models here.

class Producto(models.Model):
    numProducto = models.BigAutoField(primary_key = True)
    nombreProducto = models.CharField(max_length=100,verbose_name='Nombre del Producto')
    cantidad = models.PositiveBigIntegerField(default=1,verbose_name='Cantidad del Producto')
    cantidadMinima = models.PositiveBigIntegerField(default=1,verbose_name='Cantidad Minima del Producto')
    precio = models.PositiveBigIntegerField(default=1,verbose_name='Precio del Producto')
    descripcion = models.CharField(max_length=1000,verbose_name='Descripción del Producto')
    def __str__(self):
        return "{}".format(self.nombreProducto)
    class Meta:
        db_table = 'producto'
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'


    def generarNombre(instance,filename):
        extension = os.path.splitext(filename)[1][1:]
        ruta = 'productos'
        fecha = timezone.now().strftime("%d%m%Y_%H%M%S")
        nombre = "{}.{}".format(fecha,extension)
        return os.path.join(ruta,nombre)
    
    foto = models.ImageField(upload_to=generarNombre,null=True,default='productos/producto.jpg')


# Models Empleado
class Cargo(models.Model):
    nombre = models.CharField(max_length=100,verbose_name="Nombre del Cargo")
    creado = models.DateTimeField(default=timezone.now) # trae la fecha y hora del server

    def __str__(self):
        return "{}".format(self.nombre)

    class Meta:
        db_table = 'cargo'
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'

class Departamento(models.Model):
    codigo = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=100,verbose_name="Nombre del departamento")
    creado = models.DateTimeField(default=timezone.now) # trae la fecha y hora del server

    def __str__(self):
        return "{}".format(self.nombre)

    class Meta:
        db_table = 'departamento'
        verbose_name = 'Departamento'
        verbose_name_plural = 'Departamentos'

class Empleado(models.Model):
    run = models.CharField(max_length=10,verbose_name='RUN')
    nombre = models.CharField(max_length=50, verbose_name='Nombre')
    paterno = models.CharField(max_length=50, verbose_name='Apellido Paterno')
    materno = models.CharField(max_length=50, verbose_name='Apellido Materno')
    sexo = models.CharField(max_length=1,choices=sexos,default='o')
    codigoEmpleado = models.CharField(max_length=20,verbose_name='Código de Empleado')
    sueldo = models.PositiveIntegerField(default=450000,verbose_name='sueldo Base')
    fechaNac = models.DateField(blank=True,null=True,verbose_name='Fecha de Nacimiento')
    cargo = models.ForeignKey(Cargo,null=False,on_delete=models.RESTRICT)
    departamento = models.ForeignKey(Departamento,null=True,on_delete=models.CASCADE)
    creado = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "{} {} {}".format(self.nombre,self.paterno,self.materno)

    class Meta:
        db_table = 'empleado'
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'
        ordering = ['nombre','paterno','materno']
        
        

#RESERVA PRODUCTO

class rProducto(models.Model):
    numProducto = models.BigAutoField(primary_key = True)
    nombreProducto = models.CharField(max_length=100,verbose_name='Nombre del Producto')
    cantidad = models.PositiveBigIntegerField(default=1,verbose_name='Cantidad del Producto')
    cantidadMinima = models.PositiveBigIntegerField(default=1,verbose_name='Cantidad Minima del Producto')
    descripcion = models.CharField(max_length=1000,verbose_name='Descripción del Producto')
    def __str__(self):
        return "{}".format(self.nombreProducto)
    class Meta:
        db_table = 'rproducto'
        verbose_name = 'rProducto'
        verbose_name_plural = 'rProductos'


    def rgenerarNombre(instance,filename):
        extension = os.path.splitext(filename)[1][1:]
        ruta = 'rproductos'
        fecha = timezone.now().strftime("%d%m%Y_%H%M%S")
        nombre = "{}.{}".format(fecha,extension)
        return os.path.join(ruta,nombre)
    
    foto = models.ImageField(upload_to=rgenerarNombre,null=True,default='productos/producto.jpg')



class Usuario(models.Model):
    run = models.CharField(max_length=10,verbose_name='Run')
    nombres = models.CharField(max_length=100,verbose_name='Nombres')
    apellidos = models.CharField(max_length=50,verbose_name='Apellidos')
    sexo = models.CharField(max_length=1,choices=sexos,default='o')
    fechaNac = models.DateField(null=True,blank=True,verbose_name='Fecha de Nacimiento')
    email = models.CharField(max_length=100,verbose_name='E-mail')
    contras = models.CharField(max_length=50,verbose_name='Contraseña')
    repcontras = models.CharField(max_length=50,verbose_name='Repetir Contraseña')

    def __str__(self):
        return "{} {} {} {} {} {} {} {} ".format(self.run,self.nombres,self.apellidos,self.sexo,self.fechaNac,self.email,self.contras,self.repcontras)
    
    class Meta:
        db_table = 'usuario'
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        ordering = ['run', 'nombres', 'apellidos', 'sexo', 'fechaNac', 'email', 'contras','repcontras']