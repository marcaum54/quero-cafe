from django.core.management.base import BaseCommand

import re
from random import randint
from datetime import datetime

from core.helpers.slack import Message

from django.contrib.auth.models import User
from coffee_rotation.models import Turn
from coffee_rotation.models import Cycle


class Command(BaseCommand):
    help = "Comando escolhe um dos usuários que ainda não fizeram café."

    def handle(self, *args, **options):
        try:
            #SCHEDULES HOURS
            now = datetime.now()
            schedules = { 'morning': now.replace(hour=8, minute=0, second=0), 'afternoon': now.replace(hour=13, minute=0, second=0) }

            #ACTUAL CYCLE
            cycle = Cycle.objects.last()

            #LAST TURN
            last_turn = Turn.objects.filter(cycle=cycle, date_removed__isnull=True).last()
            penult_turn = Turn.objects.filter(cycle=cycle, date_removed__isnull=True).exclude(id=last_turn.id).last()

            #SEARCHING USERS NOT CHOOSED BEFORE
            turns = Turn.objects.filter(cycle=cycle)
            calleds = turns.filter(date_removed__isnull=True).values_list('user', flat=True)
            not_calleds = User.objects.exclude(pk__in=calleds)

            if not not_calleds.count():
                cycle = Cycle.objects.create(name=re.sub('\d(?!\d)', lambda x: str(int(x.group(0)) + 1), cycle.name))
                not_calleds = User.objects.all()

            #CHOOSED RANDOMLY
            choosed = not_calleds[randint(0, not_calleds.count() - 1)]

            #CREATING TURN
            Turn.objects.create(user=choosed, cycle=cycle, date_choosed=datetime.now())

            #ENVIANDO MENSAGEM AO GRUPO DO SLACK
            mensagem = "("+ choosed.first_name +") foi o escolhido para fazer o café."
            Message.send(text=mensagem)

        except ValueError as error:

            print(repr(error))