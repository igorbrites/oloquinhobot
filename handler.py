import json
import os
import random
import sys

here = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(here, "./vendor"))

import requests

TOKEN = os.environ['TELEGRAM_TOKEN']
BASE_URL = "https://api.telegram.org/bot{}".format(TOKEN)


def oloquinho(event, context):
    try:
        oloquinho_meu = 'https://s3.amazonaws.com/oloquinhobot/audios/oloquinho-meu.opus'
        olha_essa_ferinha_meu = 'https://s3.amazonaws.com/oloquinhobot/audios/olha-essa-ferinha-meu.opus'

        data = json.loads(event["body"])
        chat_id = data["message"]["chat"]["id"]
        text = str(data['message']['text']).replace('@oloquinhobot', '')

        if text == '/oloquinhomeu':
            audio = oloquinho_meu
        elif text == '/olhessaferaimeu':
            audio = olha_essa_ferinha_meu
        else:
            audio = random.choice([oloquinho_meu, olha_essa_ferinha_meu])

        data = {
            "chat_id": chat_id,
            "voice": audio
        }

        requests.post(f"{BASE_URL}/sendVoice", data)

    except Exception as e:
        print(e)

    return {"statusCode": 200}
