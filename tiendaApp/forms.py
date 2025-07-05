from datetime import date
import datetime
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from tiendaApp.models import Producto, rProducto, Cargo, Departamento, Empleado, Usuario
from tiendaApp.choices import sexos
import re





class ProductoForm(forms.ModelForm):
    nombreProducto = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese nombre'}))
    cantidad = forms.CharField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    cantidadMinima = forms.CharField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    precio = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    descripcion = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese Descripción'}))

    class Meta:
        model = Producto
        fields = '__all__'
    def clean_descripcion(self):
        descripcion = self.cleaned_data.get('descripcion')
        # Agrega tu lógica de validación para la descripción aquí
        # Por ejemplo, puedes verificar la longitud o cualquier otro criterio necesario
        if len(descripcion) < 10:
            raise forms.ValidationError('La descripción debe tener al menos 10 caracteres.')
        return descripcion
    
    def clean_cantidad(self):
        cantidad = self.cleaned_data.get('cantidad')
        if cantidad and int(cantidad) < 0:
            raise forms.ValidationError('La cantidad debe ser un número positivo.')
        return cantidad

    def clean_precio(self):
        precio = self.cleaned_data.get('precio')
        if precio is not None and float(precio) < 0:  # Convertir el precio a float antes de la comparación
            raise forms.ValidationError('El precio debe ser un número positivo.')
        return precio
    
    def clean_nombreProducto(self):
        nombre_producto = self.cleaned_data.get('nombreProducto')
        if not nombre_producto.replace(" ", "").isalpha():
            raise forms.ValidationError('El nombre del producto solo debe contener letras y espacios.')
        return nombre_producto

# RESERVA RODUCTO
class rProductoForm(forms.ModelForm):
    nombreProducto = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ingrese nombre'}))
    cantidad = forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control'}))
    cantidadMinima = forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control'}))
    descripcion = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ingrese Descripción'}))

    class Meta: 
        model = rProducto   
        fields = '__all__'

    def clean_cantidad(self):
        cantidad = self.cleaned_data.get('cantidad')

        # Verificar si cantidad es nula
        if cantidad is None:
            raise forms.ValidationError('La cantidad es obligatoria.')

        # Verificar si cantidad es negativa
        if int(cantidad) < 0:
            raise forms.ValidationError('La cantidad debe ser un número positivo.')

        return cantidad
    
    def clean_nombreProducto(self):
        nombre_producto = self.cleaned_data.get('nombreProducto')
        if not nombre_producto.replace(" ", "").isalpha():
            raise forms.ValidationError('El nombre del producto solo debe contener letras y espacios.')
        return nombre_producto
    
    def clean_descripcion(self):
        descripcion = self.cleaned_data.get('descripcion')
        # Agrega tu lógica de validación para la descripción aquí
        # Por ejemplo, puedes verificar la longitud o cualquier otro criterio necesario
        if len(descripcion) < 10:
            raise forms.ValidationError('La descripción debe tener al menos 10 caracteres.')
        return descripcion

class EmpleadoForm(forms.ModelForm):
    run = forms.CharField(
        widget=forms.TextInput(
        attrs={'class':'form-control','placeholder':'ingrese run'}))
    nombre = forms.CharField(widget=forms.TextInput(
        attrs={'class':'form-control','placeholder':'ingrese nombre'}))
    paterno = forms.CharField(widget=forms.TextInput(
        attrs={'class':'form-control','placeholder':'ingrese Apellido Paterno'}))
    materno = forms.CharField(widget=forms.TextInput(
        attrs={'class':'form-control','placeholder':'ingrese Apellido Materno'}))
    codigoEmpleado = forms.CharField(widget=forms.TextInput(
        attrs={'class':'form-control','placeholder':'ingrese Codigo empleado'}))
    sexo = forms.CharField(widget=forms.Select(choices=sexos,
        attrs={'class':'form-select'}))
    sueldo = forms.CharField(widget=forms.NumberInput(
        attrs={'class':'form-control'}))
    fechaNac = forms.DateField(widget=forms.DateInput(
        attrs={'class':'form-control','placeholder':'día/mes/año'}))
    
    cargo = forms.ModelChoiceField(
        queryset=Cargo.objects.all(),
        empty_label="Seleccione Cargo",
        widget=forms.Select(attrs={'class':'form-select'})
    )

    departamento = forms.ModelChoiceField(
        queryset=Departamento.objects.all(),
        empty_label="Seleccione departamento",
        widget=forms.Select(attrs={'class':'form-select'})
    )

    class Meta:
        model = Empleado
        fields = '__all__'

    def clean_sueldo(self):
        sueldo = self.cleaned_data.get('sueldo')
        if sueldo and float(sueldo) < 0:
            raise forms.ValidationError('El sueldo debe ser un número positivo.')
        return sueldo
    
    def clean_run(self):
        run = self.cleaned_data.get('run')
        if not validar_rut(run):
            raise forms.ValidationError('El RUN no tiene un formato de RUT válido.')
        return run
    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if not nombre.replace(" ", "").isalpha():
            raise forms.ValidationError('El nombre solo debe contener letras y espacios.')
        return nombre
    
    def clean_paterno(self):
        paterno = self.cleaned_data.get('paterno')
        if not paterno.replace(" ", "").isalpha():
            raise forms.ValidationError('El apellido paterno solo debe contener letras y espacios.')
        return paterno

    def clean_materno(self):
        materno = self.cleaned_data.get('materno')
        if not materno.replace(" ", "").isalpha():
            raise forms.ValidationError('El apellido materno solo debe contener letras y espacios.')
        return materno
    
    def clean_codigoEmpleado(self):
        codigo_empleado = self.cleaned_data.get('codigoEmpleado')
        if not codigo_empleado.isalnum():
            raise forms.ValidationError('El código de empleado solo debe contener caracteres alfanuméricos.')
        return codigo_empleado
    
    def clean_sexo(self):
        sexo = self.cleaned_data.get('sexo')
        if sexo not in [s[0] for s in sexos]:
            raise forms.ValidationError('Seleccione un valor válido para el sexo.')
        return sexo

def validar_rut(rut):
    # La función validar_rut debe verificar si el RUT tiene el formato correcto
    # Puedes implementar tu propia lógica de validación aquí
    # Por ejemplo, puedes usar expresiones regulares
    # Esta implementación es una aproximación simple y puede no cubrir todos los casos
    rut = rut.replace(".", "").replace("-", "")
    if not rut.isdigit() or len(rut) < 2:
        return False
    cuerpo, digito_verificador = rut[:-1], rut[-1].upper()
    if not cuerpo.isdigit():
        return False
    suma = sum(int(digito) * (2 + i % 6) for i, digito in enumerate(reversed(cuerpo)))
    resto = suma % 11
    digito_calculado = str(11 - resto) if resto != 0 else '0'
    if digito_verificador == 'K':
        return digito_calculado == '10'
    return digito_calculado == digito_verificador

class UsuarioForm(forms.ModelForm):
    run = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'ingrese rut'}))

    nombres = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'ingrese nombre'}))

    apellidos = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'ingrese apellidos'}))

    sexo = forms.CharField(widget=forms.Select(choices=sexos,attrs={'class':'form-select'}))

    fechaNac = forms.DateField(widget=forms.DateInput(attrs={'class':'form-control','placeholder':'dia/mes/años','type':'date'}))

    email = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'ingrese su E-mail'}))
    
    contras = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'ingrese su contraseña'}))

    repcontras = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'repita su contraseña'}))
    
    class Meta:
        model = Usuario
        fields = '__all__'

    def clean_contras(self):
        contraseña = self.cleaned_data.get('contras')
        if len(contraseña) < 8:
            raise forms.ValidationError('La contraseña debe tener al menos 8 caracteres.')
        return contraseña

    def clean_repcontras(self):
        contraseña = self.cleaned_data.get('contras')
        repcontraseña = self.cleaned_data.get('repcontras')
        if contraseña != repcontraseña:
            raise forms.ValidationError('Las contraseñas no coinciden.')
        return repcontraseña
    
    def clean_nombres(self):
        nombres = self.cleaned_data.get('nombres')
        if not nombres.replace(" ", "").isalpha():
            raise forms.ValidationError('El nombre debe contener solo letras y espacios.')
        return nombres
    
    def clean_run(self):
        run = self.cleaned_data.get('run').replace(".", "").replace("-", "")
        
        # Verificar que el RUT tiene el formato correcto
        if not run.isdigit() or len(run) < 7:
            raise forms.ValidationError('El RUT debe contener al menos 7 dígitos numéricos.')

        # Calcular el dígito verificador esperado
        rut_numerico = int(run[:-1])
        dv_calculado = int(run[-1])

        # Calcular el dígito verificador real
        suma = 0
        multiplicador = 2
        for digito in reversed(str(rut_numerico)):
            suma += int(digito) * multiplicador
            multiplicador = multiplicador + 1 if multiplicador < 7 else 2

        dv_real = 11 - (suma % 11)
        dv_real = dv_real if dv_real != 10 else 'K'

        # Verificar que el dígito verificador sea correcto
        if str(dv_real) != str(dv_calculado) and str(dv_calculado).upper() != 'K':
            raise forms.ValidationError('El RUT no es válido. Verifica el dígito verificador.')

        return run
    
    def clean_apellidos(self):
        apellidos = self.cleaned_data.get('apellidos')
        if not apellidos.replace(" ", "").isalpha():
            raise forms.ValidationError('Los apellidos deben contener solo letras y espacios.')
        return apellidos
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        
        # Verificar si el email tiene un formato válido
        if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
            raise forms.ValidationError('Ingrese una dirección de correo electrónico válida.')

        return email
    
    def clean_fechaNac(self):
        fecha_nacimiento = self.cleaned_data.get('fechaNac')
        
        # Verificar si la fecha de nacimiento es en el pasado
        if fecha_nacimiento and fecha_nacimiento >= date.today():
            raise forms.ValidationError('La fecha de nacimiento debe ser en el pasado.')

        return fecha_nacimiento
    

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2']
