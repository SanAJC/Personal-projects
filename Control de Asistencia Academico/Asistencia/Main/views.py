from django.shortcuts import render , redirect
from .forms import AsistenciaForm
import csv
from django.http import HttpResponse
from Main.models import Asistencia
from django.contrib.auth import authenticate, login
import qrcode 

# Create your views here.

def home(request):
    

    return render(request,'Main/home.html',{
        'title':'Bienvenido'
        }) 

#Formulario

def form(request):
    if request.method == "POST":
        form = AsistenciaForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda la instancia de Asistencia en la base de datos
            # Redirige a una página exitosa o a donde desees
            return redirect('Home')
    else:
        form = AsistenciaForm()  # Crea un formulario en blanco

    return render(request, 'Main/form.html', {
        'title': 'Formulario de Asistencia',
        'form': form,
    })
    

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if username and password:  # Comprueba si se proporcionaron el nombre de usuario y la contraseña
            if user is not None:
                login(request, user)
                return redirect('Exportar')  # Redirige a la página deseada después del inicio de sesión
            else:
                return redirect('Home')
             # Aquí puedes manejar el caso en el que las credenciales no son válidas
                

    return render(request, 'layouts/export.html',{
        'title': 'Registro'})
    

#Exportar

def export_csv(request):
    queryset=Asistencia.objects.all()
    
    options=Asistencia._meta
    fields=[field.name for field in options.fields]
    
    response=HttpResponse(content_type='text/csv')
    response['Content-Disposition']='attachment;filename="authors.csv"'
    
    writer=csv.writer(response)
    writer.writerow([options.get_field(field).verbose_name for field in fields])

    for obj in queryset:
        writer.writerow([getattr(obj,field)for field in fields])
        
    return response

def qr(request):
    qr = qrcode.QRCode(
        version = 1,
        error_correction = qrcode.constants.ERROR_CORRECT_L,
        box_size = 10,
        border = 3,
    )
    url = 'http://10.26.43.188:8000/form/'
    qr.add_data(url)
    qr.make(fit = True)
    
    img = qr.make_image(fill_color = 'black', back_color = 'transparent')
    
    response = HttpResponse(content_type = 'image/png')
    img.save(response,'PNG')
    return response


