from django.shortcuts import render
from django.conf import settings
from django.shortcuts import redirect
from django.core.urlresolvers import reverse_lazy

from django.contrib.auth.models import User
from coffee_rotation.models import Cycle
from coffee_rotation.models import Turn
from django.contrib import messages

def users_list(request):

    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (reverse_lazy('admin:login'), request.path))

    usuarios = User.objects.all()

    return render(request, 'colaboradores/index.html', {
        'usuarios': usuarios
    })

def setAsVoluntary(request):

    try:
        current_user = request.user

        cycle = Cycle.objects.last()

        turn = Turn.objects.filter(cycle=cycle, user=current_user)

        if turn:
            raise ValueError('O usuário ')

        messages.success(request, 'Profile details updated.')

    except ValueError as error:
        messages.error(request, error)

    return redirect(reverse_lazy('admin:login'))