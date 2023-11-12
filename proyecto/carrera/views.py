# views.py
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .models import Registro
from .forms import RegistroForm

# Definir la vista de registro
def registro(request):
    # Si la petición es de tipo GET, mostrar el formulario vacío
    if request.method == 'GET':
        form = RegistroForm()
        return render(request, 'registro.html', {'form': form})
    # Si la petición es de tipo POST, procesar el formulario
    elif request.method == 'POST':
        form = RegistroForm(request.POST)
        # Si el formulario es válido, guardar los datos y enviar el correo
        if form.is_valid():
            form.save()
            numero_identificacion = form.cleaned_data['numero_identificacion']
            nombres = form.cleaned_data['nombres']
            apellidos = form.cleaned_data['apellidos']
            correo_electronico = form.cleaned_data['correo_electronico']
            distancia = form.cleaned_data['distancia']
            categoria = form.cleaned_data['categoria']
            # Definir el asunto y el mensaje del correo
            asunto = 'Inscripción exitosa a la carrera'
            mensaje = f'Hola {nombres} {apellidos},\n\nTe felicitamos por tu inscripción exitosa a la carrera de {distancia} en la categoría {categoria}. Te esperamos el día de la carrera con mucha energía y entusiasmo.\n\nGracias por participar.'
            # Enviar el correo al usuario
            send_mail(asunto, mensaje, 'noreply@bing.com', [correo_electronico])
            # Redirigir a la página de éxito
            return redirect('exito')
        # Si el formulario no es válido, mostrar los errores
        else:
            return render(request, 'registro.html', {'form': form})

# Definir la vista de éxito
def exito(request):
    # Mostrar la página de éxito
    return render(request, 'exito.html')
