
from django.contrib import admin
from django.urls import path
from django.urls import path, include
from tiendaApp import views as vista


from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',vista.inicio,name='inicio'),
    path('login/',vista.login, name='login'),
    path('pdf/',vista.pdf, name='pdf'),
    path('generar_pdf/<int:num_producto>/',vista.generar_pdf, name='generar_pdf'),
    path('accounts/',include('django.contrib.auth.urls')),
    path('register/',vista.register, name='register'),
    path('catalogo/',vista.catalogo, name='catalogo'),
    path('productos/',vista.productos, name='productos'),
    path('productoAdd/',vista.productoAdd,name='productoAdd'),
    path('productoEdit/<int:numProducto>/',vista.cargar_editar_producto,name='editarProducto'),
    path('productoEditado/<int:numProducto>/',vista.editar_producto,name='productoEditado'),
    path('productoDel/<int:numProducto>/',vista.eliminar_producto,name='eliminarProducto'),
    path('empleados/',vista.todos,name='empleados'),
    path('empleadoAdd/',vista.empleadoAdd,name='crearEmpleado'),
    path('rproductos/',vista.rproductos, name='rproductos'),
    path('rproductoAdd/',vista.rproductoAdd,name='rproductoAdd'),
    path('rproductoEdit/<int:numProducto>/',vista.cargar_editar_reserva,name='reditarProducto'),
    path('rproductoEditado/<int:numProducto>/',vista.editar_reserva,name='rproductoEditado'),
    path('rproductoDel/<int:numProducto>/',vista.eliminar_reserva,name='reliminarProducto'),
    path('empleados/', vista.todos, name='empleados'),
    path('empleadoAdd/', vista.empleadoAdd, name='empleadoAdd'),
    path('empleadoEdit/<int:empleado_id>/',vista.cargar_editar_empleado,name='empleadoedit'),
    path('empleadoEditado/<int:empleado_id>/',vista.editar_empleados,name='empleadoEditado'),
    path('empleadoDel/<int:empleado_id>/',vista.eliminar_empleado,name='eliminarEmpleado'),


    

#PRODUCTOS PRINCIPALES

    path('panes/',vista.panes, name='panes'),
    path('principal/',vista.principal, name='principal'),
    path('deshidratado/',vista.deshidratado, name='deshidratado'),
    path('mermeladasymieles/',vista.mermeladasymieles, name='mermeladasymieles'),
    path('pasteles/',vista.pasteles, name='pasteles'),
    path('tartaletas/',vista.tartaletas, name='tartaletas'),
    path('embutidosylacteos/',vista.embutidosylacteos, name='embutidosylacteos'),
    path('120/',vista.moto120, name='120'),
    path('435/',vista.moto435, name='435'),
    path('445-e-series/',vista.moto445e,name='445-e-series'),
    path('445ii/',vista.moto445ii,name='445ii'),
    path('61/',vista.moto61,name='61'),
    path('3120xp/',vista.moto3120xp,name='3120xp'),
    path('525pts/',vista.pod525pt,name='525pts'),
    path('100pts/',vista.pod100pt,name='100pts'),
    path('101pts/',vista.pod101pt,name='101pts'),
    path('200pts/',vista.mimer200pt,name='200pts'),
    path('201pts/',vista.mimer201pt,name='201pts'),
    path('202pts/',vista.mimer202pt,name='202pts'),
    path('300pts/',vista.pastel300pt,name='300pts'),
    path('301pts/',vista.pastel301pt,name='301pts'),
    path('302pts/',vista.pastel302pt,name='302pts'),
    path('400pts/',vista.tarta400pt,name='400pts'),
    path('401pts/',vista.tarta401pt,name='401pts'),
    path('402pts/',vista.tarta402pt,name='402pts'),
    path('500pts/',vista.embutidos500pt,name='500pts'),
    path('501pts/',vista.embutidos501pt,name='501pts'),
    path('502pts/',vista.embutidos502pt,name='502pts'),

    path('usuarios/',vista.usuarios,name='usuarios'),
    path('usuariosAdd/',vista.usuariosAdd,name='usuariosAdd'),
    path('usuarioEdit/<int:usuario_id>/',vista.cargar_editar_usuarios,name='usuarioEdit'),
    path('usuarioEditado/<int:usuario_id>/',vista.editar_usuarios,name='usuarioEditado'),
    path('usuarioDel/<int:usuario_id>/',vista.eliminar_usuario,name='eliminarUsuario'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) 


