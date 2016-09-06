from django.core.management.base import BaseCommand
from random import randint
from datetime import datetime
import requests

#MODELS
from colaboradores.models import Colaborador

class Command(BaseCommand):
    help = "Comando escolhe um dos colaboradores que ainda não fizeram café."

    def handle(self, *args, **options):
        try:
            colaboradores = Colaborador.objects.using('default').filter(flag_date__isnull=True)

            if not colaboradores:
                colaboradores = Colaborador.objects.all()

                if not colaboradores:
                    raise ValueError('Não existem colaboradores cadastrados')

                #ZERANDO A FLAG DE DATA DE TODOS OS COLABORADORES
                colaboradores.update(flag_date=None)

            #ESCOLHENDO COLABORADOR ALEATORIAMENTE
            random_index = randint(0, colaboradores.count() - 1)
            colaborador_escolhido = colaboradores[random_index]

            #ADICIONANDO DATA DE CHAMADA DO COLABORADOR ESCOLHIDO
            colaborador_escolhido.flag_date = datetime.now()
            colaborador_escolhido.save()

            mensagem = "@"+ colaborador_escolhido.slack_nickname + " ("+ colaborador_escolhido.name +") foi o escolhido para fazer o café."

            #ENVIANDO MENSAGEM AO GRUPO DO SLACK
            # curl -X POST --data-urlencode 'payload={"channel": "#quero-cafe", "username": "Véi Do Café", "text": "{FULANO} vai fazer o café", "icon_emoji": ":coffee:"}' https://hooks.slack.com/services/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
            url = 'https://hooks.slack.com/services/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'
            payload = {"channel": "#quero-cafe", "username": "Véi Do Café", "text": mensagem, "icon_emoji": ":coffee:"}
            response = requests.post(url, data=payload, headers={})

        except ValueError as error:
            print(repr(error))