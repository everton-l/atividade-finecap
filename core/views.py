from multiprocessing import context
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ReservaForm, Reserva
# Create your views here.


def index(request):
    reserva = Reserva.objects.all()
    context = {'reservas':reserva}
    return render(request, 'index.html', context)

def reserva_criar(request):
    if request.method == 'POST':
        form = ReservaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = ReservaForm()
            return redirect('index')
            
    else:
        form = ReservaForm()

    return render(request, 'form.html', context={'form':form})

def reserva_remover(request, id):
    reserva = get_object_or_404(Reserva, id=id)
    reserva.delete()
    return redirect('index')


def reserva_detalhe(request, id):
    reserva = get_object_or_404(Reserva, id=id)
    return render(request, 'detalhe.html', context={'reserva':reserva})