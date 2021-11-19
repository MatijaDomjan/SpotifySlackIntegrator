import requests
import json



def slack_sending_message():
    df = SelectSongsFrame()
    webhook = 'https://hooks.slack.com/services/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'
    data = {
        "text": """Bok Matac, zadnjih tjedan dana najviše ti se dopala pjesma """ +  df['song_name']  + """" od """ + ['artist']+ ""

    }
    try:
        response = requests.post(webhook,json.dumps(data))
    except:
        'Greska prilikom slanja poruke'
    return 1

if __name__ == "__main__":
    slack_sending_message()