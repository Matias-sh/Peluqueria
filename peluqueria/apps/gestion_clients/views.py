from django.shortcuts import render, redirect
from .models import Cliente, Tratamiento
from .forms import ClienteForm, TratamientoForm

def dashboard(request):
    clientes = Cliente.objects.all()
    return render(request, 'gestion_clients/dashboard.html', {'clientes': clientes})

def cliente_detalle(request, pk):
    cliente = Cliente.objects.get(pk=pk)
    tratamientos = Tratamiento.objects.filter(cliente=cliente)
    return render(request, 'gestion_clients/cliente_detalle.html', {'cliente': cliente, 'tratamientos': tratamientos})

def agregar_cliente(request):
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = ClienteForm()
    return render(request, 'gestion_clients/agregar_cliente.html', {'form': form})

def agregar_tratamiento(request):
    if request.method == "POST":
        form = TratamientoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = TratamientoForm()
    return render(request, 'gestion_clients/agregar_tratamiento.html', {'form': form})
