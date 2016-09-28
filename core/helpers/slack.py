import requests

class Message:

    def send(text, username="CAFEITICEIRA" ,emoji=":coffee:", channel="#quero-cafe"):

        url = 'https://hooks.slack.com/services/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'
        payload = { "channel": channel, "username": username, "text": text, "icon_emoji": emoji }
        response = requests.post(url, data=payload, headers={})

        return response