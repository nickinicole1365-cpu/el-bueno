from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template.loader import render_to_string
from weasyprint import HTML
from .models import Task
from .forms import CreateNewTask


# Función auxiliar para calcular restante
def calcular_restante(task):
    if task.total is not None and task.anticipo is not None:
        return task.total - task.anticipo
    return 0


def home(request):
    tasks = Task.objects.filter(activo=True)

    for task in tasks:
        task.restante = calcular_restante(task)

    return render(request, 'index.html', {'task': tasks})


def Create_task(request):
    if request.method == 'POST':
        form = CreateNewTask(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.activo = True  # 🔥 fuerza activo siempre
            task.save()
            return redirect('/home/')
    else:
        form = CreateNewTask()

    return render(request, 'create_task.html', {'form': form})


def delete_task(request, id):
    if request.method == 'POST':
        task = get_object_or_404(Task, id=id)
        task.activo = False  # soft delete
        task.save()
    return redirect('/home/')


def edit_task(request, id):
    task = get_object_or_404(Task, id=id)
    if request.method == 'POST':
        task.Product = request.POST.get('Product', task.Product)
        task.descripcion = request.POST.get('descripcion', task.descripcion)
        task.estado = request.POST.get('estado', task.estado)
        task.nombre = request.POST.get('nombre', task.nombre)
        task.numero_telefono = request.POST.get('numero_telefono', task.numero_telefono)
        task.tipografia = request.POST.get('tipografia', task.tipografia)
        task.anticipo = request.POST.get('anticipo', task.anticipo)
        task.total = request.POST.get('total', task.total)

        fecha = request.POST.get('fecha')
        if fecha:
            task.fecha = fecha

        hora = request.POST.get('hora')
        if hora:
            task.hora = hora

        task.save()
        return redirect('/home/')
    
    return render(request, 'edit_task.html', {'task': task})
    
    return render(request, 'edit_task.html', {'task': task})


def ver(request, id):
    task = get_object_or_404(Task, id=id)
    task.restante = calcular_restante(task)
    return render(request, 'ver.html', {'task': task})


def descargar_nota_pdf(request, id):
    task = get_object_or_404(Task, id=id)
    task.restante = calcular_restante(task)

    html_string = render_to_string('ver.html', {'task': task})

    pdf = HTML(
        string=html_string,
        base_url=request.build_absolute_uri('/')
    ).write_pdf()

    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="nota_pedido_{task.id:04d}.pdf"'
    return response


def SinPrevio(request):
    tasks = Task.objects.filter(estado='Sin previo', activo=True)

    for task in tasks:
        task.restante = calcular_restante(task)

    return render(request, 'SinPrevio.html', {'task': tasks})


def EnGrabado(request):
    tasks = Task.objects.filter(estado='Grabando', activo=True)

    for task in tasks:
        task.restante = calcular_restante(task)

    return render(request, 'grabando.html', {'task': tasks})


def Entregar(request):
    tasks = Task.objects.filter(estado='Entregar', activo=True)

    for task in tasks:
        task.restante = calcular_restante(task)

    return render(request, 'Entregar.html', {'task': tasks})