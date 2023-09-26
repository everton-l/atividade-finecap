from multiprocessing import context
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ReservaForm, Reserva
# Create your views here.


def index(request):
    reserva = Reserva.objects.all()

    nome_empresa = request.GET.get('nome_empresa')
    quitado = request.GET.get('quitado')
    valor_stand = request.GET.get('valor_stand')
    data_reserva = request.GET.get('data_reserva')

    if nome_empresa:
        reserva = reserva.filter(nome_empresa__icontains=nome_empresa)
    if quitado is not None:
        reserva = reserva.filter(quitado=quitado)
    if valor_stand is not None and valor_stand != '':
        reserva = reserva.filter(stand__valor=valor_stand)
    if data_reserva:
        reserva = reserva.filter(data_reserva=data_reserva)

    context = {
        'reservas': reserva,
        'nome_empresa': nome_empresa,
        'quitado': quitado,
        'valor_stand': valor_stand,
        'data_reserva': data_reserva,
    }

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