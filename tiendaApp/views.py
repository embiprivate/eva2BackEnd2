from django.shortcuts import render,redirect
from tiendaApp.forms import EmpleadoForm
from tiendaApp.models import Empleado,Cargo,Departamento,Usuario
# Create your views here.
from django.contrib.auth.decorators import permission_required, login_required
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.template.loader import get_template

from django.http import HttpResponse, Http404

from django.contrib.auth import login

from tiendaApp import models as datos

from tiendaApp.models import Producto
from tiendaApp.models import rProducto
from tiendaApp.forms import ProductoForm,UsuarioForm
from tiendaApp.forms import rProductoForm
from django.shortcuts import get_object_or_404

def inicio(request):
    anuncios = {
        1: {'imagen': 'amasadox.jpeg', 'texto': '¡Descubre nuestras deliciosas opciones de pan!'},
        2: {'imagen': 'duri.jpg', 'texto': '¡Promoción especial en pasteles este mes!'},
        3: {'imagen': 'tar.jpg', 'texto': '¡Distintos sabores de Tartaletas!'},
        # Agrega más anuncios según sea necesario
    }
    return render(request, 'inicio.html', {'anuncios': anuncios})

@login_required
def login(request):
    return render(request,'registration/login.html')

def register(request):
    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        user_creation_form = CustomUserCreationForm(data=request.POST)
        if user_creation_form.is_valid():
            user_creation_form.save()

            return redirect('inicio')
        

    return render(request, 'registration/register.html', data)


def pdf(request):
    return render(request,'pdf.html')
def catalogo(request):
    return render(request,'catalogo.html')

@permission_required('tiendaApp.view_producto')
def productos(request):
    if request.method == 'POST':  # Cambio aquí para verificar si el método es POST
        texto = request.POST.get('buscar')  # Corregido para usar .get() en lugar de request.POST['buscar']
        if texto:
            productos = Producto.objects.filter(nombreProducto__icontains=texto)
        else:
            productos = Producto.objects.all()
    else:
        productos = Producto.objects.all()

    data = {
        'productos': productos,
    }
    return render(request, 'productos.html', data)

@permission_required('tiendaApp.add_producto')
def productoAdd(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('productos')  # Reemplaza 'nombre_de_tu_vista_redirigida' con el nombre de tu vista
    else:
        form = ProductoForm()

    return render(request, 'productoAdd.html', {'form': form})
    
@permission_required('tiendaApp.change_producto')
def cargar_editar_producto(request, numProducto):
    producto = get_object_or_404(Producto,numProducto=numProducto)
    form = ProductoForm(instance=producto)

    return render(request, 'productoEdit.html', {'form':form, 'producto':producto})

@permission_required('tiendaApp.change_producto')
def editar_producto(request, numProducto):
    producto = get_object_or_404(Producto,numProducto=numProducto)

    if request.method == 'POST':
        form = ProductoForm(request.POST,request.FILES, instance=producto)
        if form.is_valid():
            if 'foto' in request.FILES:
                producto.foto = request.FILES['foto']
            form.save()
            return redirect('/productos/')
    
    else:
        form = ProductoForm(instance=producto)

    return render(request, 'productoEdit.html', {'form': form, 'producto': producto})


@permission_required('tiendaApp.delete_producto')
def eliminar_producto(request, numProducto):
    producto = get_object_or_404(Producto,numProducto=numProducto)

    if request.method == 'POST':
        producto.delete()
        return redirect('/productos/')

    return render(request, 'productoDel.html', {'producto':producto})


#VISTAS RESERVA PRODUCTOS
@permission_required('tiendaApp.view_rproducto')
def rproductos(request):
    if request.method == 'POST':  # Cambio aquí para verificar si el método es POST
        texto = request.POST.get('buscar')  # Corregido para usar .get() en lugar de request.POST['buscar']
        if texto:
            rproductos = rProducto.objects.filter(nombreProducto__icontains=texto)
        else:
            rproductos = rProducto.objects.all()
    else:
        rproductos = rProducto.objects.all()

    data = {
        'rproductos': rproductos,
    }
    return render(request, 'rproductos.html', data)

@permission_required('tiendaApp.add_rproducto')
def rproductoAdd(request):
    if request.method == 'POST':
        form = rProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('rproductos')  # Reemplaza 'nombre_de_tu_vista_redirigida' con el nombre de tu vista
    else:
        form = rProductoForm()

    return render(request, 'rproductoAdd.html', {'form': form})
    

def cargar_editar_reserva(request, numProducto):
    rproducto = get_object_or_404(rProducto,numProducto=numProducto)
    form = rProductoForm(instance=rproducto)

    return render(request, 'rproductoEdit.html', {'form':form, 'rproducto':rproducto})

@permission_required('tiendaApp.change_rproducto')
def editar_reserva(request, numProducto):
    rproducto = get_object_or_404(rProducto,numProducto=numProducto)

    if request.method == 'POST':
        form = rProductoForm(request.POST,request.FILES, instance=rproducto)
        if form.is_valid():
            if 'foto' in request.FILES:
                rproducto.foto = request.FILES['foto']
            form.save()
            return redirect('/rproductos/')
    
    else:
        form = rProductoForm(instance=rproducto)

    return render(request, 'rproductoEdit.html', {'form': form, 'rproducto': rproducto})


@permission_required('tiendaApp.delete_rproducto')
def eliminar_reserva(request, numProducto):
    rproducto = get_object_or_404(rProducto,numProducto=numProducto)

    if request.method == 'POST':
        rproducto.delete()
        return redirect('/rproductos/')

    return render(request, 'rproductoDel.html', {'rproducto':rproducto})


# Vistas Empleado
@permission_required('tiendaApp.view_empleado')
def todos(request):
    cargos = Cargo.objects.all()
    departamentos = Departamento.objects.all()
    empleados = Empleado.objects.all()
    data = {
        'empleados':empleados,
        'cargos':cargos,
        'departamentos':departamentos,
    }
    return render(request,'empleados.html',data)

@permission_required('tiendaApp.add_empleado')
def empleadoAdd(request):
    if request.method == 'POST':
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/empleados/')  
    else:
        form = EmpleadoForm()
    return render(request, 'empleadoAdd.html', {'form': form})


def cargar_editar_empleado(request, empleado_id):
    empleados= get_object_or_404(empleados,id=empleado_id)
    form = EmpleadoForm(instance=empleados)


    return render(request, 'empleadoEdit.html', {'form': form,'empleado':empleados})


def editar_empleados(request, empleado_id):
    empleados = get_object_or_404(Empleado,id=empleado_id)

    if request.method == 'POST':
        form = EmpleadoForm(request.POST, instance=empleados)
        if form.is_valid():
            form.save()
            return redirect('/empleados/')

    else:
        form = EmpleadoForm(instance=empleados)

    return render(request, 'empleadoEdit.html', {'form': form})


def eliminar_empleado(request, empleado_id):
    empleado = get_object_or_404(Empleado, id=empleado_id)
    
    if request.method == 'POST':
        empleado.delete()
        return redirect('/empleados/')
    
    return render(request, 'empleadoDel.html',{'empleado':empleado})


#USUARIOS
def usuarios(request):
    usuarios = Usuario.objects.all()
    data = {
        'usuarios':usuarios,
        
    }
    return render(request,'usuarios.html',data)

def usuariosAdd(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('usuarios')  # Cambia 'usuarios.html' a 'usuarios'
    else:
        form = UsuarioForm()
    return render(request, 'usuariosAdd.html', {'form': form})



def cargar_editar_usuarios(request, usuario_id):
    usuarios= get_object_or_404(Usuario,id=usuario_id)
    form = UsuarioForm(instance=usuarios)


    return render(request, 'usuariosEdit.html', {'form': form,'usuario':usuarios})


def editar_usuarios(request, usuario_id):
    usuarios = get_object_or_404(Usuario,id=usuario_id)

    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=usuarios)
        if form.is_valid():
            form.save()
            return redirect('/usuarios/')

    else:
        form = UsuarioForm(instance=usuarios)

    return render(request, 'usuariosEdit.html', {'form': form})

def eliminar_usuario(request, usuario_id):
    usuario = get_object_or_404(Usuario, id=usuario_id)
    
    if request.method == 'POST':
        usuario.delete()
        return redirect('/usuarios/')
    
    return render(request, 'usuarioDel.html',{'usuario':usuario})



#VISTAS PRODUCTOS EJEMPLOS

def principal(request):
    return render(request, 'principal.html')

def panes(request):
    return render(request, 'panes.html')

def deshidratado(request):
    return render(request, 'deshidratado.html')

def mermeladasymieles(request):
    return render(request, 'mermeladasymieles.html')

def pasteles(request):
    return render(request, 'pasteles.html')

def tartaletas(request):
    return render(request, 'tartaletas.html')

def embutidosylacteos(request):
    return render(request, 'embutidosylacteos.html')

def moto120(request):
    data = {
        'tipo':'Pan Marraqueta',
        'calorias':'291kcal',
        'grasa':'1,30g',
        'carbh':'60,00g',
        'prot':'8,20g'
    }
    return render(request,'motos/moto120.html',data)

def moto435(request):
    data = {
        'tipo':'Hallulla',
        'calorias':'309kcal',
        'grasa':'4,00g',
        'carbh':'61,60g',
        'prot':'8,20g'
    }
    return render(request,'motos/moto435.html',data)

def moto445e(request):
    data = {
        'tipo':'Pan Blanco',
        'calorias':'64kcal',
        'grasa':'0,88g',
        'carbh':'11,97g',
        'prot':'1,98g'
    }
    return render(request,'motos/moto445e.html',data)

def moto445ii(request):
    data = {
        'tipo':'Pan Rollo',
        'calorias':'243kcal',
        'grasa':'4,15g',
        'carbh':'42,82g',
        'prot':'7,69g'
    }
    return render(request,'motos/moto445ii.html',data)

def moto61(request):
    data = {
        'tipo':'Amasado',
        'calorias':'247kcal',
        'grasa':'6,47g',
        'carbh':'40,82g',
        'prot':'5,63g'
    }
    return render(request,'motos/moto61.html',data)

def moto3120xp(request):
    data = {
        'tipo':'Pan Baguette',
        'calorias':'175kcal',
        'grasa':'1,92g',
        'carbh':'33,22g',
        'prot':'5,63g'
    }
    return render(request, 'motos/moto3120xp.html',data)

def pod525pt(request):
    data = {
        'tipo':'Naranja',
        'calorias':'270kcal',
        'grasa':'6,4g',
        'carbh':'79,82g',
        'prot':'3,63g'
    }
    return render(request, 'podadoresAlt/525pt.html',data)

def pod100pt(request):
    data = {
        'tipo':'Platano',
        'calorias':'368kcal',
        'grasa':'6,5g',
        'carbh':'82,88g',
        'prot':'3,44g'
    }
    return render(request, 'podadoresAlt/100pt.html',data)

def pod101pt(request):
    data = {
        'tipo':'Frutilla',
        'calorias':'350kcal',
        'grasa':'6,0g',
        'carbh':'83,88g',
        'prot':'3,50g'
    }
    return render(request, 'podadoresAlt/101pt.html',data)

def mimer200pt(request):
    data = {
        'tipo':'Frutilla',
        'calorias':'358kcal',
        'grasa':'6,0g',
        'carbh':'80,0g',
        'prot':'3,50g'
    }
    return render(request, 'mimer/200pt.html',data)

def mimer201pt(request):
    data = {
        'tipo':'Miel',
        'calorias':'338kcal',
        'grasa':'3,0g',
        'carbh':'73,88g',
        'prot':'2,50g'
    }
    return render(request, 'mimer/201pt.html',data)

def mimer202pt(request):
    data = {
        'tipo':'Durazno',
        'calorias':'360kcal',
        'grasa':'6,5g',
        'carbh':'83,88g',
        'prot':'4,0g'
    }
    return render(request, 'mimer/202pt.html',data)

def pastel300pt(request):
    data = {
        'tipo':'Piña',
        'calorias':'300kcal',
        'grasa':'4,5g',
        'carbh':'73,88g',
        'prot':'6,0g'
    }
    return render(request, 'pastel/300pt.html',data)

def pastel301pt(request):
    data = {
        'tipo':'Durazno',
        'calorias':'360kcal',
        'grasa':'5,5g',
        'carbh':'63,88g',
        'prot':'4,0g'
    }
    return render(request, 'pastel/301pt.html',data)

def pastel302pt(request):
    data = {
        'tipo':'Chocolate',
        'calorias':'400kcal',
        'grasa':'6,5g',
        'carbh':'85,88g',
        'prot':'5,0g'
    }
    return render(request, 'pastel/302pt.html',data)

def tarta400pt(request):
    data = {
        'tipo':'Frutilla',
        'calorias':'300kcal',
        'grasa':'3,5g',
        'carbh':'80,88g',
        'prot':'4,0g'
    }
    return render(request, 'tarta/400pt.html',data)

def tarta401pt(request):
    data = {
        'tipo':'Durazno',
        'calorias':'400kcal',
        'grasa':'5,5g',
        'carbh':'75,88g',
        'prot':'5,0g'
    }
    return render(request, 'tarta/401pt.html',data)

def tarta402pt(request):
    data = {
        'tipo':'Chocolate',
        'calorias':'500kcal',
        'grasa':'7,5g',
        'carbh':'87,88g',
        'prot':'5,0g'
    }
    return render(request, 'tarta/402pt.html',data)

def embutidos500pt(request):
    data = {
        'tipo':'Lacteo',
        'calorias':'400kcal',
        'grasa':'3,5g',
        'carbh':'40,88g',
        'prot':'6,0g'
    }
    return render(request, 'embutidos/500pt.html',data)

def embutidos501pt(request):
    data = {
        'tipo':'Embutido',
        'calorias':'300kcal',
        'grasa':'5,5g',
        'carbh':'67,88g',
        'prot':'3,0g'
    }
    return render(request, 'embutidos/501pt.html',data)

def embutidos502pt(request):
    data = {
        'tipo':'Embutido',
        'calorias':'400kcal',
        'grasa':'6,5g',
        'carbh':'77,88g',
        'prot':'5,0g'
    }
    return render(request, 'embutidos/502pt.html',data)


def generar_pdf(request, num_producto):
    print(f'Número de producto: {num_producto}')  # Agrega esta línea para depuración

    try:
        rproducto = get_object_or_404(Producto, numProducto=num_producto)
    except Http404:
        return HttpResponse('No existe el Producto', status=404)

    template_path = 'pdf.html'  # Ruta a tu template HTML para el PDF
    context = {'rproducto': rproducto}  # Contexto para pasar a la plantilla del PDF

    # Creamos un objeto HttpResponse con las cabeceras del PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{rproducto.nombreProducto}_detalle.pdf"'

    # Cargamos la plantilla del PDF
    template = get_template(template_path)
    html = template.render(context)

    # Creamos el PDF
    pisaStatus = pisa.CreatePDF(html, dest=response)

    # Si el PDF se creó correctamente, retornamos la respuesta
    if pisaStatus.err:
        return HttpResponse('Error al generar el PDF', status=500)
    return response