from django.shortcuts import render, redirect
from .models import Event
from .forms import EventForm
from django.contrib import messages

def event_list(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event_name = form.cleaned_data.get('name_event')
            try:
                nombre = Event.objects.get(name_event=event_name)
                print(f"Evento duplicado: {nombre.name_event}")  
                messages.error(request, 'Evento ya existe.')
            except Event.DoesNotExist:
                form.save()
                print("Evento guardado exitosamente")  # Depuración
                messages.success(request, 'Evento registrado con éxito.')
                return redirect('event_list')
        else:
            print("Formulario no es válido")
    else:
        form = EventForm()
    
    events = Event.objects.all()
    return render(request, 'eventos/event_list.html', {'form': form, 'events': events})

def edit_event(request, event_id):
    try:
        event = Event.objects.get(id=event_id)
    except Event.DoesNotExist:
        messages.error(request, 'El evento no existe.')
        return redirect('event_list')

    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            messages.success(request, 'Evento actualizado con éxito.')
            return redirect('event_list')
    else:
        form = EventForm(instance=event)
    return render(request, 'eventos/edit_event.html', {'form': form})

def confirm_delete_event(request, event_id):
    try:
        event = Event.objects.get(id=event_id)
    except Event.DoesNotExist:
        messages.error(request, 'El evento no existe.')
        return redirect('event_list')
    
    if request.method == 'POST':
        event.delete()
        messages.success(request, 'El evento ha sido eliminado con éxito.')
        return redirect('event_list')
    
    return render(request, 'eventos/confirm_delete_event.html', {'event': event})

def delete_event(request, event_id):
    try:
        event = Event.objects.get(id=event_id)
    except Event.DoesNotExist:
        messages.error(request, 'El evento no existe.')
        return redirect('event_list')
    
    event.delete()
    messages.success(request, 'El evento ha sido eliminado con éxito.')
    return redirect('event_list')
