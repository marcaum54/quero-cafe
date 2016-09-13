from django.core.management.base import BaseCommand

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
            #ACTUAL CYCLE
            actual_cycle = Cycle.objects.last()

            #IF NOT / CREATING FIRST CYCLE
            if not actual_cycle:
                actual_cycle = Cycle.objects.create(name='WEEK 01')

            #SEARCHING VOLUNTARY
            choosed_user = User.objects.filter(turn__cycle=actual_cycle, turn__voluntary_date__isnull=False).order_by('turn__voluntary_date').first()

            #WITHOUT VOLUNTARY
            if not choosed_user:
                #SEARCHING USERS NOT CHOOSED BEFORE
                usuarios = User.objects.filter(turn__cycle=actual_cycle, turn__cycle__isnull=True)

                if not usuarios:
                    usuarios = User.objects.all()

                    if not usuarios:
                        raise ValueError('Não existem usuarios cadastrados')

                    Turn.objects.filter(cycle=actual_cycle).update(deleted_at=datetime.now())

                    #CREATING NEW CYCLE
                    actual_cycle = Cycle.objects.create(name='WEEK ' + '{0:02}'.format(actual_cycle.id))

                #ESCOLHENDO COLABORADOR ALEATORIAMENTE
                random_index = randint(0, usuarios.count() - 1)
                choosed_user = usuarios[random_index]

            #ADICIONANDO DATA DE CHAMADA DO COLABORADOR ESCOLHIDO
            Turn.objects.create(user=choosed_user, cycle=actual_cycle, made_date=datetime.now())

            mensagem = "@"+ choosed_user.slack_nickname + " ("+ choosed_user.name +") foi o escolhido para fazer o café."

            #ENVIANDO MENSAGEM AO GRUPO DO SLACK
            Message.send(text=mensagem)

        except ValueError as error:
            print(repr(error))