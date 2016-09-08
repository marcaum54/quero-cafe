from django.shortcuts import render
from colaboradores.models import Colaborador


def colaborators_list(request):
    rows = Colaborador.objects.order_by('flag_date', 'name').all()

    return render(request, 'colaboradores/index.html', {
        'rows': rows
    })


def justify(request):

    s = ''